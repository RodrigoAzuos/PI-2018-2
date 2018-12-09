from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Base(models.Model):

    criado_em = models.DateTimeField('Criado em', auto_now_add=True, blank=False, null=False)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True

    def get_criado_em(self, format):
        return self.criado_em.__format__(format).__str__()

    def get_atualizado_em(self, format):
        return self.atualizado_em.__format__(format).__str__()


class Perfil(Base):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    sexo = models.CharField('Sexo', max_length=16, choices=SEXO_CHOICES, blank=False, null=False)
    telefone = models.CharField('Telefone', max_length=16, blank=False, null=False)
    data_nascimento = models.DateField('Data de nascimento', blank=False, null=False)
    usuario = models.OneToOneField(User, on_delete= models.CASCADE, related_name='perfil')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return "%s %s" % (self.nome(), self.sobrenome())

    def nome(self):
        return self.usuario.first_name

    def sobrenome(self):
        return self.usuario.last_name

class Post(Base):

    titulo =  models.CharField('Titulo', max_length=128, null=False, blank=False)
    resumo = models.CharField('Resumo', max_length=10000, null=False, blank=False)
    palavras_chave = models.CharField('Palavra_chave', max_length=255, null=False, blank=False)
    autor = models.ForeignKey(Perfil, null=False, blank=False, on_delete=models.CASCADE, related_name='posts')
    coautor = models.ManyToManyField(Perfil, related_name='contribuicoes')
    curtidas = models.ManyToManyField(Perfil, related_name='posts_curtidos')
    area_tematica = models.ForeignKey('AreaTematica', on_delete=models.CASCADE, related_name='posts')
    aceito = models.BooleanField('Aceito', default=False)
    tipo = models.ForeignKey('Tipo', on_delete=models.CASCADE, related_name='posts')
    arquivo = models.FileField('Arquivo', upload_to='arquivos/%Y/', null=True,blank=True)
    foto = models.ImageField('Foto', upload_to='imagens/%Y/',null=True,blank=True)

class Tipo(Base):

    nome = models.CharField('Tipo', max_length=255, null=False, blank=False)
    descricao = models.CharField('Descricao', max_length=255, null=False, blank=False)

    def __str__(self):
        return '%s' %(self.nome)

class AreaTematica(Base):

    nome = models.CharField('Tipo', max_length=255, null=False, blank=False)
    descricao = models.CharField('Descricao', max_length=255, null=False, blank=False)

    def __str__(self):
        return '%s - %s' %(self.nome, self.descricao)

class Comentario(Base):

    descricao = models.CharField('Descricao', max_length=256, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comentarios', blank=False, null=False)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.descricao




