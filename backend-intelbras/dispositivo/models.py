from django.db import models
from simple_history.models import HistoricalRecords

from area.models import Area


class Dispositivo(models.Model):
    
    CONTROLADORA_1_PORTA = 'C1PORTA'
    CONTROLADORA_2_PORTA = 'C2PORTA'
    CONTROLADORA_4_PORTA = 'C4PORTA'
    PULL_SDK = 'PULL'
    STD_SDK = 'STD'
    TIPO_CONTROLADOR_ACESSO_CHOICES = (
        (CONTROLADORA_1_PORTA, 'Controladora 1 Porta'),
        (CONTROLADORA_2_PORTA, 'Controladora 2 Portas'),
        (CONTROLADORA_4_PORTA, 'Controladora 4 Portas'),
        (PULL_SDK, 'Disp.PullSDK'),
        (STD_SDK, 'Disp.PullSDK'),
    )
    
    TCPIP = 'TCPIP'
    SERIAL = 'SERIAL'
    COMUNICACAO_CHOICES = (
        (TCPIP, 'TCP/IP'),
        (SERIAL, 'RS486'),
    )
    
    COM1 = 'COM1'
    COM2 = 'COM2'
    COM3 = 'COM3'
    PORTA_SERIAL_CHOICES = (
        (COM1, 'COM1'),
        (COM2, 'COM2'),
        (COM3, 'COM3'),
    )
    
    BR9600 = '9600'
    BR19200 = '19200'
    BR38400 = '38400'
    BR57600 = '57600'
    BR115200 = '115200'
    BAUD_RATE_CHOICES = (
        (BR9600, '9600'),
        (BR19200, '19200'),
        (BR38400, '38400'),
        (BR57600, '57600'),
        (BR115200, '115200'),
    )
    
    nome = models.CharField(max_length=250)
    possui_senha = models.BooleanField('Possui Senha', default=False)
    senha = models.CharField('Senha Comunicação', max_length=250, null=True)
    tipo_controle = models.CharField('Tipo de Controle de Acesso', max_length=7, choices=TIPO_CONTROLADOR_ACESSO_CHOICES, default=CONTROLADORA_1_PORTA)
    troca_bidirecional = models.BooleanField('Troca para Duas-Portas Bidirecional', default=False)
    sincronismo_hora = models.BooleanField('Sincronismo automático de Hora', default=True)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    excluir_dados = models.BooleanField('Excluir Dados do Dispositivo ao Adicionar', default=False)
    modo_comunicacao = models.CharField('Modo Comunicação', max_length=6, choices=COMUNICACAO_CHOICES, default=TCPIP)
    ip = models.GenericIPAddressField('Endereço IP', protocol='IPv4', null=True)
    porta = models.IntegerField('Porta IP', null=True)
    porta_serial = models.CharField('Num. Porta Serial', max_length=6, choices=PORTA_SERIAL_CHOICES, default=COM1, null=True)
    endereco = models.IntegerField('Endereço RS485', null=True)
    baud_rate = models.CharField('Baud Rate', max_length=6, choices=BAUD_RATE_CHOICES, default=BR9600, null=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return '%s' % (self.nome)