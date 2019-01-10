from django.db import models
from simple_history.models import HistoricalRecords

from dispositivo.models import Dispositivo
from usuario.models import Usuario
from visitante.models import Visitante
from zonatempo.models import ZonaTempo


class PerfilAcesso(models.Model):
    
    nome = models.CharField(max_length=250)
    zona_tempo = models.ForeignKey(ZonaTempo, on_delete=models.DO_NOTHING)
    usar_visitas = models.BooleanField('Usar em Visitas', default=True)
    dispositivos = models.ManyToManyField(Dispositivo)
    usuarios = models.ManyToManyField(Usuario)
    visitantes = models.ManyToManyField(Visitante)
    history = HistoricalRecords()
    
    def __str__(self):
        return '%s' % (self.nome)