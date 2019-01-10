from django.db import models
from simple_history.models import HistoricalRecords


class Departamento(models.Model):
    nome = models.CharField(max_length=30)
    numero = models.CharField(max_length=30)
    departamento_principal = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.nome
