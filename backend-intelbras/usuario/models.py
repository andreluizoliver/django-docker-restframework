from django.db import models
from simple_history.models import HistoricalRecords

from departamento.models import Departamento
from pessoa.models import Pessoa


class Usuario(models.Model):
    
    FUNCIONARIO = 'F'
    ADMINISTRADOR = 'A'
    TIPO_USUARIO_CHOICES = (
        (FUNCIONARIO, 'Funcionário'),
        (ADMINISTRADOR, 'Administrador'),
    )
    
    pessoa = models.OneToOneField(Pessoa, on_delete=models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING)
    tipo_usuario = models.CharField('Tipo de Usuário', max_length=1, choices=TIPO_USUARIO_CHOICES, default=FUNCIONARIO)
    data_contratacao = models.DateField('Data de Contratação')
    history = HistoricalRecords()
    
    def __str__(self):
        return '%s' % (self.pessoa)
