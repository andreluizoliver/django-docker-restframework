from django.db import models
from simple_history.models import HistoricalRecords

from pessoa.models import Pessoa


class Visitante(models.Model):
    
    pessoa = models.OneToOneField(Pessoa, on_delete=models.DO_NOTHING)
    history = HistoricalRecords()
    
    def __str__(self):
        return '%s' % (self.pessoa)