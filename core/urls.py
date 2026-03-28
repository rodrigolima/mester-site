from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    # PROJETOS: conteudo de pre-aprovados (projetos para patrocinio)
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/<slug:slug>/', views.projeto_detalhe, name='projeto_detalhe'),
    # DOCUMENTARIOS: cases realizados (antigo Projetos + Audiovisual unificados)
    path('documentarios/', views.documentarios, name='documentarios'),
    path('documentarios/<slug:slug>/', views.documentario_detalhe, name='documentario_detalhe'),
    # LIVROS
    path('livros/', views.livros, name='livros'),
    # EDUCACAO
    path('educacao/', views.educacao, name='educacao'),
    # SOBRE (antigo Quem Somos)
    path('sobre/', views.sobre, name='sobre'),
    # CONTATO (movido para footer, mas pagina ainda existe)
    path('contato/', views.contato, name='contato'),
    path('privacidade/', views.privacidade, name='privacidade'),
]
