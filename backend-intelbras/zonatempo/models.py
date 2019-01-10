from django.db import models
from simple_history.models import HistoricalRecords


class ZonaTempo(models.Model):
    
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250, null=True)
    
    def __str__(self):
        return '%s' % (self.nome)

class Tempo(models.Model):
    
    DOMINGO = 1
    SEGUNDA = 2
    TERCA = 3
    QUARTA = 4
    QUINTA = 5
    SEXTA = 6
    SABADO = 7    
    DIA_SEMANA_CHOICES = (
        (DOMINGO, 'Domingo'),
        (SEGUNDA, 'Segunda-feira'),
        (TERCA, 'Terça-feira'),
        (QUARTA, 'Quarta-feira'),
        (QUINTA, 'Quinta-feira'),
        (SEXTA, 'Sexta-feira'),
        (SABADO, 'Sábado'),
    )
    
    zona_tempo = models.ForeignKey(ZonaTempo, on_delete=models.CASCADE)
    dia_semana = models.IntegerField('Dia da semana', choices=DIA_SEMANA_CHOICES, default=SEGUNDA)
    inicio = models.TimeField('Início')
    fim = models.TimeField('Fim')
    history = HistoricalRecords()
    
    def __str__(self):
        return '%s %s : %s - %s' % (self.zona_tempo.nome, self.dia_semana, self.inicio, self.fim)

