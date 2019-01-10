from django.db import models
from simple_history.models import HistoricalRecords

from pessoa.models import Pessoa


class Endereco(models.Model):
    
    RESIDENCIAL = 'R'
    COMERCIAL = 'C'
    TIPO_ENDERECO = (
        (RESIDENCIAL, 'Residencial'),
        (COMERCIAL, 'Comercial'),
    )
    
    UF_CHOICES = (
        ('AC', 'Acre'), 
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    tipo_endereco = models.CharField(max_length=1, choices=TIPO_ENDERECO, default=RESIDENCIAL)
    uf = models.CharField('UF', max_length=2, choices=UF_CHOICES, default='SC')
    cidade = models.CharField(max_length=250)
    cep = models.BigIntegerField('CEP')
    rua = models.CharField(max_length=250)
    numero = models.IntegerField('Número')
    bairro = models.CharField(max_length=250)
    complemento = models.CharField(max_length=250, null=True) 
    history = HistoricalRecords() 
    
    def __str__(self):
        return '%s, %s, %s, %s - %s, %s' % (self.rua, self.numero, self.bairro, self.cidade, self.uf, self.cep)
