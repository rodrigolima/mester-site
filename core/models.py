from django.db import models


class Video(models.Model):
    CATEGORIA_CHOICES = [
        ('documentario', 'Documentário'),
        ('institucional', 'Institucional'),
        ('educacional', 'Educacional'),
        ('branded', 'Branded Content'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField('Título', max_length=200)
    descricao = models.TextField('Descrição', blank=True)
    categoria = models.CharField(
        'Categoria', max_length=30,
        choices=CATEGORIA_CHOICES, default='documentario',
    )
    bunny_embed_url = models.URLField(
        'URL do Player Bunny',
        help_text='Cole aqui a URL de embed do Bunny Stream (ex: https://iframe.mediadelivery.net/embed/...)',
    )
    thumbnail = models.ImageField(
        'Thumbnail',
        upload_to='videos/thumbnails/',
        blank=True,
        help_text='Imagem de capa do vídeo. Recomendado: 16:9 (ex: 1280×720).',
    )
    destaque = models.BooleanField('Destaque na home', default=False)
    ativo = models.BooleanField('Ativo', default=True)
    ordem = models.PositiveIntegerField('Ordem', default=0)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['ordem', '-criado_em']
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'

    def __str__(self):
        return self.titulo


class Livro(models.Model):
    CATEGORIA_CHOICES = [
        ('arte', 'Livro de Arte'),
        ('fotografia', 'Fotografia'),
        ('documentario', 'Documentário'),
        ('institucional', 'Institucional'),
        ('educacional', 'Educacional'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField('Título', max_length=200)
    subtitulo = models.CharField('Subtítulo', max_length=300, blank=True)
    descricao = models.TextField('Descrição')
    categoria = models.CharField(
        'Categoria', max_length=30,
        choices=CATEGORIA_CHOICES, default='arte',
    )
    capa = models.ImageField(
        'Imagem de Capa',
        upload_to='livros/capas/',
        help_text='Foto principal do livro para o card. Recomendado: 3:4 (ex: 600×800).',
    )
    ano = models.PositiveIntegerField('Ano de publicação', blank=True, null=True)
    autor = models.CharField('Autor(es)', max_length=300, blank=True)
    destaque = models.BooleanField('Destaque na home', default=False)
    ativo = models.BooleanField('Ativo', default=True)
    ordem = models.PositiveIntegerField('Ordem', default=0)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['ordem', '-criado_em']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo


class FotoLivro(models.Model):
    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='fotos',
        verbose_name='Livro',
    )
    imagem = models.ImageField(
        'Imagem',
        upload_to='livros/fotos/',
        help_text='Foto do livro (páginas, detalhes, etc).',
    )
    legenda = models.CharField('Legenda', max_length=300, blank=True)
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Foto do Livro'
        verbose_name_plural = 'Fotos do Livro'

    def __str__(self):
        return f'{self.livro.titulo} — Foto {self.ordem}'
