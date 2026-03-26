from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase
from image_uploader_widget.admin import OrderedImageUploaderInline
from image_uploader_widget.widgets import ImageUploaderWidget
from .models import Video, Livro, FotoLivro, PaginaLivro, Projeto, FotoProjeto, ProjetoPreAprovado


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'destaque', 'ativo', 'ordem', 'criado_em')
    list_editable = ('destaque', 'ativo', 'ordem')
    list_filter = ('categoria', 'destaque', 'ativo')
    search_fields = ('titulo', 'descricao')
    ordering = ('ordem', '-criado_em')


class FotoLivroInline(OrderedImageUploaderInline):
    model = FotoLivro
    order_field = 'ordem'
    fields = ('imagem', 'legenda', 'ordem')
    verbose_name = 'Foto'
    verbose_name_plural = '📷 Fotos do livro  (mosaico da página)'


class PaginaLivroInline(OrderedImageUploaderInline):
    model = PaginaLivro
    order_field = 'ordem'
    fields = ('imagem', 'ordem')
    verbose_name = 'Página'
    verbose_name_plural = '📖 Páginas do livro  (visualizador estilo Amazon)'


@admin.register(Livro)
class LivroAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('capa_preview', 'titulo', 'categoria', 'ano', 'num_fotos', 'num_paginas', 'destaque', 'ativo', 'ordem')
    list_editable = ('destaque', 'ativo', 'ordem')
    list_filter = ('categoria', 'destaque', 'ativo')
    search_fields = ('titulo', 'subtitulo', 'descricao', 'autor')
    ordering = ('ordem', '-criado_em')
    inlines = [FotoLivroInline, PaginaLivroInline]

    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }

    fieldsets = (
        ('Informações', {
            'fields': ('titulo', 'subtitulo', 'descricao', 'categoria', 'autor', 'ano'),
        }),
        ('Capa', {
            'fields': ('capa',),
        }),
        ('Publicação', {
            'fields': ('destaque', 'ativo', 'ordem'),
        }),
    )

    def capa_preview(self, obj):
        if obj.capa:
            return format_html(
                '<img src="{}" style="height:60px;width:auto;border-radius:2px;'
                'object-fit:cover;box-shadow:0 2px 6px rgba(0,0,0,.25);">',
                obj.capa.url,
            )
        return '—'
    capa_preview.short_description = 'Capa'

    def num_fotos(self, obj):
        n = obj.fotos.count()
        return f'{n} foto{"s" if n != 1 else ""}'
    num_fotos.short_description = 'Fotos'

    def num_paginas(self, obj):
        n = obj.paginas.count()
        return f'{n} pág.'
    num_paginas.short_description = 'Páginas'


class FotoProjetoInline(OrderedImageUploaderInline):
    model = FotoProjeto
    order_field = 'ordem'
    fields = ('imagem', 'legenda', 'ordem')
    verbose_name = 'Foto'
    verbose_name_plural = '📷 Fotos do projeto'


@admin.register(Projeto)
class ProjetoAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'categoria', 'ano', 'destaque', 'ativo', 'ordem')
    list_editable = ('destaque', 'ativo', 'ordem')
    list_filter = ('tipo', 'categoria', 'destaque', 'ativo')
    search_fields = ('titulo', 'descricao', 'sinopse', 'diretor', 'produtor')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('ordem', '-criado_em')
    inlines = [FotoProjetoInline]


@admin.register(ProjetoPreAprovado)
class ProjetoPreAprovadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'categoria', 'pronac', 'valor', 'tem_detalhe', 'ativo', 'ordem')
    list_editable = ('tem_detalhe', 'ativo', 'ordem')
    list_filter = ('tipo', 'categoria', 'tem_detalhe', 'ativo')
    search_fields = ('titulo', 'descricao', 'pronac')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('categoria', 'ordem')
