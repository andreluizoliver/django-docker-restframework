from cpffield import cpffield
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords


class Pessoa(models.Model):
    
    MASCULINO = 'M'
    FEMININO = 'F'
    SEXO_CHOICES = (
        (MASCULINO, 'Maculino'),
        (FEMININO, 'Feminino'),
    )
    
    SOLTEIRO = 'SO'
    CASADO = 'CA'
    SEPARADO = 'SE'
    DIVORCIADO = 'DI'
    VIUVO = 'VI'
    ESTADO_CIVIL_CHOICES = (
        (SOLTEIRO, 'Solteiro(a)'),
        (CASADO, 'Casado(a)'),
        (SEPARADO, 'Separado(a)'),
        (DIVORCIADO, 'Divorciado(a)'),
        (VIUVO, 'Viúvo(a)'),
    )
    
    nome = models.CharField(max_length=250)
    sobrenome = models.CharField(max_length=250)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default=MASCULINO)
    email = models.EmailField(max_length=254)
    telefone_celular = PhoneNumberField(null=True, blank=True)
    telefone_residencial = PhoneNumberField(null=True, blank=True)
    telefone_comercial = PhoneNumberField(null=True, blank=True)
    data_nascimento = models.DateField(null=True)
    cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
    estado_civil = models.CharField(max_length=2, choices=ESTADO_CIVIL_CHOICES, default=SOLTEIRO)
    rg = models.BigIntegerField(null=True)
    nacionalidade = models.CharField(max_length=250, null=True)
    foto = models.ImageField(upload_to='pessoa/foto', height_field=None, width_field=None, max_length=100, null=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return '%s %s' % (self.nome, self.sobrenome)