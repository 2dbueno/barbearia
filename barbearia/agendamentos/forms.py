from django import forms
from django.contrib.auth.models import User
from .models import Agendamento, Barbeiro, Servico
from usuarios.models import Profile
from datetime import datetime, timedelta, time

class AgendamentoForm(forms.ModelForm):
    """Formulário para agendamento de horários pelos clientes"""
    
    class Meta:
        model = Agendamento
        fields = ['barbeiro', 'servico', 'data', 'horario', 'observacoes']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.Select(),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar apenas barbeiros ativos
        self.fields['barbeiro'].queryset = Barbeiro.objects.filter(ativo=True)
        
        # Configurar as opções de horário (a cada 30 minutos)
        horarios = []
        inicio = time(9, 0)  # 9:00
        fim = time(19, 0)    # 19:00
        atual = inicio
        
        while atual <= fim:
            horarios.append((atual.strftime('%H:%M'), atual.strftime('%H:%M')))
            # Adicionar 30 minutos
            hora, minuto = atual.hour, atual.minute
            minuto += 30
            if minuto >= 60:
                hora += 1
                minuto -= 60
            atual = time(hora, minuto)
        
        self.fields['horario'].widget.choices = horarios
    
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        horario = cleaned_data.get('horario')
        barbeiro = cleaned_data.get('barbeiro')
        
        # Verificar se a data não é no passado
        if data and data < datetime.now().date():
            raise forms.ValidationError("Não é possível agendar para uma data no passado.")
        
        # Verificar se o horário já está ocupado para este barbeiro
        if data and horario and barbeiro:
            if Agendamento.objects.filter(barbeiro=barbeiro, data=data, horario=horario).exists():
                raise forms.ValidationError("Este horário já está ocupado para o barbeiro selecionado.")
        
        return cleaned_data

class AdminAgendamentoForm(forms.ModelForm):
    """Formulário para agendamento de horários pelo administrador"""
    cpf = forms.CharField(max_length=14, label='CPF do Cliente')
    
    class Meta:
        model = Agendamento
        fields = ['barbeiro', 'servico', 'data', 'horario', 'observacoes']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.Select(),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar apenas barbeiros ativos
        self.fields['barbeiro'].queryset = Barbeiro.objects.filter(ativo=True)
        
        # Configurar as opções de horário (a cada 30 minutos)
        horarios = []
        inicio = time(9, 0)  # 9:00
        fim = time(19, 0)    # 19:00
        atual = inicio
        
        while atual <= fim:
            horarios.append((atual.strftime('%H:%M'), atual.strftime('%H:%M')))
            # Adicionar 30 minutos
            hora, minuto = atual.hour, atual.minute
            minuto += 30
            if minuto >= 60:
                hora += 1
                minuto -= 60
            atual = time(hora, minuto)
        
        self.fields['horario'].widget.choices = horarios
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        try:
            profile = Profile.objects.get(cpf=cpf)
            return cpf
        except Profile.DoesNotExist:
            raise forms.ValidationError("Cliente com este CPF não encontrado.")
    
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        horario = cleaned_data.get('horario')
        barbeiro = cleaned_data.get('barbeiro')
        
        # Verificar se a data não é no passado
        if data and data < datetime.now().date():
            raise forms.ValidationError("Não é possível agendar para uma data no passado.")
        
        # Verificar se o horário já está ocupado para este barbeiro
        if data and horario and barbeiro:
            if Agendamento.objects.filter(barbeiro=barbeiro, data=data, horario=horario).exists():
                raise forms.ValidationError("Este horário já está ocupado para o barbeiro selecionado.")
        
        return cleaned_data
    
    def save(self, commit=True):
        agendamento = super().save(commit=False)
        cpf = self.cleaned_data.get('cpf')
        profile = Profile.objects.get(cpf=cpf)
        agendamento.cliente = profile
        
        if commit:
            agendamento.save()
        
        return agendamento
