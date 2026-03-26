from django.db import models
from django.urls import reverse


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
        'URL do Player Bunny (iframe)',
        help_text='URL de embed do Bunny Stream (ex: https://iframe.mediadelivery.net/embed/...)',
    )
    bunny_video_url = models.URLField(
        'URL direta do vídeo (MP4)',
        blank=True,
        help_text='URL direta do arquivo MP4 no Bunny CDN (ex: https://vz-XXXXX.b-cdn.net/VIDEO_ID/play_720p.mp4). Usada como vídeo de fundo no hero.',
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


class Projeto(models.Model):
    TIPO_CHOICES = [
        ('documentario', 'Documentário'),
        ('livro', 'Livro de Arte'),
        ('institucional', 'Institucional'),
        ('educacional', 'Educacional'),
        ('branded', 'Branded Content'),
        ('outro', 'Outro'),
    ]
    CATEGORIA_CHOICES = [
        ('sustentabilidade', 'Sustentabilidade'),
        ('brasilidade', 'Brasilidade'),
        ('inovacao', 'Inovação'),
        ('cultura', 'Cultura'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True)
    descricao = models.TextField('Descrição')
    sinopse = models.TextField('Sinopse', blank=True)
    tipo = models.CharField(
        'Tipo', max_length=30,
        choices=TIPO_CHOICES, default='documentario',
    )
    categoria = models.CharField(
        'Categoria', max_length=30,
        choices=CATEGORIA_CHOICES, default='sustentabilidade',
    )
    ano = models.PositiveIntegerField('Ano', blank=True, null=True)
    duracao = models.CharField('Duração', max_length=50, blank=True)
    formato = models.CharField('Formato', max_length=100, blank=True)
    diretor = models.CharField('Diretor(a)', max_length=200, blank=True)
    produtor = models.CharField('Produtor(a)', max_length=200, blank=True)
    fotografia = models.CharField('Fotografia', max_length=200, blank=True)
    edicao = models.CharField('Edição', max_length=200, blank=True)
    trilha_sonora = models.CharField('Trilha Sonora', max_length=200, blank=True)
    poster = models.ImageField(
        'Poster',
        upload_to='projetos/posters/',
        blank=True,
        help_text='Imagem principal do projeto. Recomendado: 16:9 (ex: 1280×720).',
    )
    bunny_embed_url = models.URLField(
        'URL do Player Bunny (iframe)',
        blank=True,
        help_text='URL de embed do Bunny Stream para o filme do projeto.',
    )
    patrocinador = models.CharField('Patrocinador', max_length=300, blank=True)
    destaque = models.BooleanField('Destaque', default=False)
    ativo = models.BooleanField('Ativo', default=True)
    ordem = models.PositiveIntegerField('Ordem', default=0)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['ordem', '-criado_em']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('core:projeto_detalhe', kwargs={'slug': self.slug})


class FotoProjeto(models.Model):
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='fotos',
        verbose_name='Projeto',
    )
    imagem = models.ImageField(
        'Imagem',
        upload_to='projetos/fotos/',
        help_text='Foto do projeto (bastidores, cenas, etc).',
    )
    legenda = models.CharField('Legenda', max_length=300, blank=True)
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Foto do Projeto'
        verbose_name_plural = 'Fotos do Projeto'

    def __str__(self):
        return f'{self.projeto.titulo} — Foto {self.ordem}'


class ProjetoPreAprovado(models.Model):
    TIPO_CHOICES = [
        ('documentario', 'Documentário'),
        ('livro', 'Livro de Arte e Fotografia'),
    ]
    CATEGORIA_CHOICES = [
        ('sustentabilidade', 'Sustentabilidade'),
        ('brasilidade', 'Brasilidade'),
        ('diversos', 'Diversos'),
    ]

    titulo = models.CharField('Título', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True)
    descricao = models.TextField('Descrição')
    conceito = models.TextField('Conceito', blank=True,
        help_text='Texto detalhado sobre o conceito do projeto (para página de detalhe).')
    tipo = models.CharField(
        'Tipo', max_length=30,
        choices=TIPO_CHOICES, default='documentario',
    )
    categoria = models.CharField(
        'Categoria', max_length=30,
        choices=CATEGORIA_CHOICES, default='sustentabilidade',
    )
    pronac = models.CharField('PRONAC', max_length=20)
    valor = models.CharField('Valor', max_length=50,
        help_text='Ex: R$ 889 mil')
    duracao = models.CharField('Duração / Formato', max_length=100, blank=True,
        help_text='Ex: 52 min, 70 min, Livro de arte e fotografia')
    imagem = models.ImageField(
        'Imagem',
        upload_to='pre_aprovados/fotos/',
        blank=True,
        help_text='Foto principal do projeto para o card.',
    )
    contrapartidas = models.TextField('Contrapartidas', blank=True,
        help_text='Lista de contrapartidas específicas do projeto (para detalhe).')
    sobre_autor = models.TextField('Sobre o Autor', blank=True,
        help_text='Texto sobre o autor/diretor (para detalhe).')
    tem_detalhe = models.BooleanField('Tem página de detalhe', default=False,
        help_text='Marque para habilitar a página de detalhe deste projeto.')
    ativo = models.BooleanField('Ativo', default=True)
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['categoria', 'ordem']
        verbose_name = 'Projeto Pré-Aprovado'
        verbose_name_plural = 'Projetos Pré-Aprovados'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('core:pre_aprovado_detalhe', kwargs={'slug': self.slug})
