from django.shortcuts import render
from .models import Video, Livro


def home(request):
    from .models import Video
    video_destaque = Video.objects.filter(ativo=True).first()
    return render(request, 'core/home.html', {'video_destaque': video_destaque})


def projetos(request):
    return render(request, 'core/projetos.html')


def audiovisual(request):
    videos = Video.objects.filter(ativo=True)
    return render(request, 'core/audiovisual.html', {'videos': videos})


def livros(request):
    livros = Livro.objects.filter(ativo=True).prefetch_related('fotos')
    return render(request, 'core/livros.html', {'livros': livros})


def quem_somos(request):
    return render(request, 'core/quem_somos.html')


def contato(request):
    return render(request, 'core/contato.html')


def privacidade(request):
    return render(request, 'core/privacidade.html')
