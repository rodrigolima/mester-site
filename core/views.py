from django.shortcuts import render
from .models import Video, Livro


def home(request):
    from .models import Video
    video_destaque = Video.objects.filter(ativo=True).first()
    return render(request, 'core/home.html', {'video_destaque': video_destaque})


def projetos(request):
    return render(request, 'core/projetos.html')


def audiovisual(request):
    todos = Video.objects.filter(ativo=True)
    video_hero = todos.filter(destaque=True).first() or todos.first()
    outros_videos = todos.exclude(pk=video_hero.pk) if video_hero else todos

    return render(request, 'core/audiovisual.html', {
        'video_hero': video_hero,
        'outros_videos': outros_videos,
    })


def livros(request):
    todos = Livro.objects.filter(ativo=True).prefetch_related('fotos')
    livro_destaque = todos.filter(destaque=True).first() or todos.first()
    outros_livros  = todos.exclude(pk=livro_destaque.pk) if livro_destaque else todos
    return render(request, 'core/livros.html', {
        'livro_destaque': livro_destaque,
        'outros_livros':  outros_livros,
        'livros': todos,
    })


def quem_somos(request):
    return render(request, 'core/quem_somos.html')


def contato(request):
    return render(request, 'core/contato.html')


def privacidade(request):
    return render(request, 'core/privacidade.html')
