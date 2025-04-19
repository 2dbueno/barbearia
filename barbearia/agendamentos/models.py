from django.db import models
from usuarios.models import Profile

class Barbeiro(models.Model):
    """Modelo para barbeiros"""
    nome = models.CharField(max_length=100, verbose_name='Nome')
    foto = models.ImageField(upload_to='barbeiros', verbose_name='Foto')
    descricao = models.TextField(verbose_name='Descrição')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Barbeiro'
        verbose_name_plural = 'Barbeiros'

class Servico(models.Model):
    """Modelo para serviços oferecidos"""
    TIPO_CHOICES = (
        ('corte', 'Corte de Cabelo'),
        ('barba', 'Barba'),
        ('bigode', 'Bigode'),
        ('combo', 'Combo (Corte + Barba)'),
    )
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name='Tipo')
    descricao = models.TextField(verbose_name='Descrição')
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço')
    duracao = models.IntegerField(default=30, verbose_name='Duração (minutos)')
    
    def __str__(self):
        return self.get_tipo_display()
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

class Agendamento(models.Model):
    """Modelo para agendamentos"""
    cliente = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='agendamentos', verbose_name='Cliente')
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE, related_name='agendamentos', verbose_name='Barbeiro')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='agendamentos', verbose_name='Serviço')
    data = models.DateField(verbose_name='Data')
    horario = models.TimeField(verbose_name='Horário')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    data_agendamento = models.DateTimeField(auto_now_add=True, verbose_name='Data do Agendamento')
    
    def __str__(self):
        return f'{self.cliente.user.username} - {self.barbeiro.nome} - {self.data} {self.horario}'
    
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        # Garantir que não haja dois agendamentos para o mesmo barbeiro no mesmo horário
        unique_together = ['barbeiro', 'data', 'horario']
