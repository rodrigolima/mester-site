from django.shortcuts import render, get_object_or_404
from .models import Video, Livro, Projeto, ProjetoPreAprovado


def home(request):
    video_destaque = Video.objects.filter(ativo=True).first()
    return render(request, 'core/home.html', {'video_destaque': video_destaque})


def projetos(request):
    todos = Projeto.objects.filter(ativo=True)
    projeto_destaque = todos.filter(destaque=True).first() or todos.first()
    outros_projetos = todos.exclude(pk=projeto_destaque.pk) if projeto_destaque else todos
    return render(request, 'core/projetos.html', {
        'projeto_destaque': projeto_destaque,
        'outros_projetos': outros_projetos,
    })


def projeto_detalhe(request, slug):
    projeto = get_object_or_404(Projeto, slug=slug, ativo=True)
    fotos = projeto.fotos.all()
    relacionados = Projeto.objects.filter(
        ativo=True, categoria=projeto.categoria
    ).exclude(pk=projeto.pk)[:3]
    return render(request, 'core/projeto_detalhe.html', {
        'projeto': projeto,
        'fotos': fotos,
        'relacionados': relacionados,
    })


def pre_aprovados(request):
    todos = ProjetoPreAprovado.objects.filter(ativo=True)
    categorias = [
        ('Sustentabilidade', [p for p in todos if p.categoria == 'sustentabilidade']),
        ('Brasilidade', [p for p in todos if p.categoria == 'brasilidade']),
        ('Diversos', [p for p in todos if p.categoria == 'diversos']),
    ]
    return render(request, 'core/pre_aprovados.html', {
        'categorias': categorias,
    })


def pre_aprovado_detalhe(request, slug):
    projeto = get_object_or_404(ProjetoPreAprovado, slug=slug, ativo=True, tem_detalhe=True)
    return render(request, 'core/pre_aprovado_detalhe.html', {
        'projeto': projeto,
    })


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
