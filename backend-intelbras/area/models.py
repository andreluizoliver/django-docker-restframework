from django.db import models
from simple_history.models import HistoricalRecords


class Area(models.Model):
    nome = models.CharField(max_length=30)
    numero = models.CharField(max_length=30)
    area_principal = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.nome
