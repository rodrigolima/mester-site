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
    livros = Livro.objects.filter(ativo=True).prefetch_related('fotos')
    return render(request, 'core/livros.html', {'livros': livros})


def quem_somos(request):
    return render(request, 'core/quem_somos.html')


def contato(request):
    return render(request, 'core/contato.html')


def privacidade(request):
    return render(request, 'core/privacidade.html')
