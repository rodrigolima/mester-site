from django.shortcuts import render, get_object_or_404
from .models import Video, Livro, Projeto, ProjetoPreAprovado


def home(request):
    video_destaque = Video.objects.filter(ativo=True).first()
    return render(request, 'core/home.html', {'video_destaque': video_destaque})


def projetos(request):
    """PROJETOS: exibe projetos para patrocinio (antigo pre-aprovados)."""
    todos = ProjetoPreAprovado.objects.filter(ativo=True)
    categorias = [
        ('Sustentabilidade', [p for p in todos if p.categoria == 'sustentabilidade']),
        ('Brasilidade', [p for p in todos if p.categoria == 'brasilidade']),
        ('Diversos', [p for p in todos if p.categoria == 'diversos']),
    ]
    return render(request, 'core/projetos.html', {
        'categorias': categorias,
    })


def projeto_detalhe(request, slug):
    """Detalhe de projeto para patrocinio (antigo pre-aprovado detalhe)."""
    projeto = get_object_or_404(ProjetoPreAprovado, slug=slug, ativo=True, tem_detalhe=True)
    return render(request, 'core/projeto_detalhe.html', {
        'projeto': projeto,
    })


def documentarios(request):
    """DOCUMENTARIOS: cases realizados (antigo Projetos + Audiovisual unificados)."""
    # Projetos (cases com ficha tecnica)
    todos_projetos = Projeto.objects.filter(ativo=True)
    projeto_destaque = todos_projetos.filter(destaque=True).first() or todos_projetos.first()
    outros_projetos = todos_projetos.exclude(pk=projeto_destaque.pk) if projeto_destaque else todos_projetos

    # Videos
    todos_videos = Video.objects.filter(ativo=True)
    video_hero = todos_videos.filter(destaque=True).first() or todos_videos.first()
    outros_videos = todos_videos.exclude(pk=video_hero.pk) if video_hero else todos_videos

    return render(request, 'core/documentarios.html', {
        'projeto_destaque': projeto_destaque,
        'outros_projetos': outros_projetos,
        'video_hero': video_hero,
        'outros_videos': outros_videos,
    })


def documentario_detalhe(request, slug):
    """Detalhe de um documentario/case realizado."""
    projeto = get_object_or_404(Projeto, slug=slug, ativo=True)
    fotos = projeto.fotos.all()
    episodios = projeto.episodios.all()
    relacionados = Projeto.objects.filter(
        ativo=True, categoria=projeto.categoria
    ).exclude(pk=projeto.pk)[:3]
    return render(request, 'core/documentario_detalhe.html', {
        'projeto': projeto,
        'fotos': fotos,
        'episodios': episodios,
        'relacionados': relacionados,
    })


def livros(request):
    todos = Livro.objects.filter(ativo=True).prefetch_related('fotos', 'paginas')
    livro_destaque = todos.filter(destaque=True).first() or todos.first()
    outros_livros = todos.exclude(pk=livro_destaque.pk) if livro_destaque else todos
    return render(request, 'core/livros.html', {
        'livro_destaque': livro_destaque,
        'outros_livros': outros_livros,
        'livros': todos,
    })


def educacao(request):
    return render(request, 'core/educacao.html')


def sobre(request):
    return render(request, 'core/quem_somos.html')


def contato(request):
    return render(request, 'core/contato.html')


def privacidade(request):
    return render(request, 'core/privacidade.html')
