from django.contrib import admin
from .models import Video, Livro, FotoLivro, Projeto, FotoProjeto, ProjetoPreAprovado


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'destaque', 'ativo', 'ordem', 'criado_em')
    list_editable = ('destaque', 'ativo', 'ordem')
    list_filter = ('categoria', 'destaque', 'ativo')
    search_fields = ('titulo', 'descricao')
    ordering = ('ordem', '-criado_em')


class FotoLivroInline(admin.TabularInline):
    model = FotoLivro
    extra = 3
    fields = ('imagem', 'legenda', 'ordem')
    ordering = ('ordem',)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'ano', 'destaque', 'ativo', 'ordem')
    list_editable = ('destaque', 'ativo', 'ordem')
    list_filter = ('categoria', 'destaque', 'ativo')
    search_fields = ('titulo', 'subtitulo', 'descricao', 'autor')
    ordering = ('ordem', '-criado_em')
    inlines = [FotoLivroInline]


class FotoProjetoInline(admin.TabularInline):
    model = FotoProjeto
    extra = 3
    fields = ('imagem', 'legenda', 'ordem')
    ordering = ('ordem',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
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
