from django.contrib import admin
from .models import Video, Livro, FotoLivro


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
