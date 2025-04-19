from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta
from .models import Agendamento, Servico, Barbeiro
from .forms import AgendamentoForm, AdminAgendamentoForm
from usuarios.models import Profile
from usuarios.decorators import admin_required

@login_required
def listar_agendamentos(request):
    """View para listar os agendamentos do usuário logado"""
    agendamentos = Agendamento.objects.filter(cliente=request.user.profile).order_by('data', 'horario')
    return render(request, 'agendamentos/listar_agendamentos.html', {'agendamentos': agendamentos})

@login_required
def agendar(request):
    """View para o cliente agendar um horário"""
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.cliente = request.user.profile
            agendamento.save()
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm()
    
    return render(request, 'agendamentos/agendar.html', {'form': form})

@login_required
def cancelar_agendamento(request, agendamento_id):
    """View para cancelar um agendamento"""
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    
    # Verificar se o agendamento pertence ao usuário logado ou se é admin
    if agendamento.cliente.user == request.user or request.user.is_staff:
        agendamento.delete()
        messages.success(request, 'Agendamento cancelado com sucesso!')
    else:
        messages.error(request, 'Você não tem permissão para cancelar este agendamento.')
    
    if request.user.is_staff:
        return redirect('admin_agendamentos')
    return redirect('listar_agendamentos')

@admin_required
def admin_agendamentos(request):
    """View para o admin visualizar todos os agendamentos"""
    agendamentos = Agendamento.objects.all().order_by('data', 'horario')
    return render(request, 'agendamentos/admin_agendamentos.html', {'agendamentos': agendamentos})

@admin_required
def admin_agendamentos_dia(request):
    """View para o admin visualizar agendamentos do dia"""
    hoje = datetime.now().date()
    agendamentos = Agendamento.objects.filter(data=hoje).order_by('horario')
    return render(request, 'agendamentos/admin_agendamentos_dia.html', {'agendamentos': agendamentos, 'data': hoje})

@admin_required
def admin_agendamentos_semana(request):
    """View para o admin visualizar agendamentos da semana"""
    hoje = datetime.now().date()
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timedelta(days=6)
    agendamentos = Agendamento.objects.filter(data__range=[inicio_semana, fim_semana]).order_by('data', 'horario')
    return render(request, 'agendamentos/admin_agendamentos_semana.html', 
                 {'agendamentos': agendamentos, 'inicio': inicio_semana, 'fim': fim_semana})

@admin_required
def admin_agendamentos_mes(request):
    """View para o admin visualizar agendamentos do mês"""
    hoje = datetime.now().date()
    inicio_mes = hoje.replace(day=1)
    if hoje.month == 12:
        fim_mes = hoje.replace(year=hoje.year + 1, month=1, day=1) - timedelta(days=1)
    else:
        fim_mes = hoje.replace(month=hoje.month + 1, day=1) - timedelta(days=1)
    
    agendamentos = Agendamento.objects.filter(data__range=[inicio_mes, fim_mes]).order_by('data', 'horario')
    return render(request, 'agendamentos/admin_agendamentos_mes.html', 
                 {'agendamentos': agendamentos, 'inicio': inicio_mes, 'fim': fim_mes})

@admin_required
def admin_agendar(request, cpf):
    """View para o admin agendar para um cliente pelo CPF"""
    if request.method == 'POST':
        form = AdminAgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save()
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('admin_agendamentos')
    else:
        form = AdminAgendamentoForm(initial={'cpf': cpf})
    
    return render(request, 'agendamentos/admin_agendar.html', {'form': form})
