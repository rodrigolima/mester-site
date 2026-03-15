from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('audiovisual/', views.audiovisual, name='audiovisual'),
    path('livros/', views.livros, name='livros'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('contato/', views.contato, name='contato'),
    path('privacidade/', views.privacidade, name='privacidade'),
]
