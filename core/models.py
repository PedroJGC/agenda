from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Criando os campos do Banco de Dados
class Evento(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField(blank=True, null=True)
  data_evento = models.DateTimeField(verbose_name='Data do Evento')
  data_criação = models.DateTimeField(auto_now=True) # insere a hora do registro atualmente
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'evento' # exigindo que o nome da tabela seja "evento"

  # função que mostra o titulo da tabela
  def __str__(self):
      return self.titulo
