from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileForm
from .decorators import admin_required

def cadastro(request):
    """View para cadastro de novos usuários"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Fazer login automático após o cadastro
            login(request, user)
            messages.success(request, f'Conta criada com sucesso! Bem-vindo, {user.first_name}!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

@login_required
def perfil(request):
    """View para exibir e atualizar perfil do usuário"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'usuarios/perfil.html', context)

@login_required
def dashboard(request):
    """View para o painel do usuário"""
    # Obter próximo agendamento e histórico
    proximo_agendamento = None
    ultimo_agendamento = None
    total_agendamentos = 0
    
    if hasattr(request.user, 'profile'):
        from agendamentos.models import Agendamento
        from datetime import datetime
        
        # Próximo agendamento (futuro)
        hoje = datetime.now().date()
        agendamentos_futuros = Agendamento.objects.filter(
            cliente=request.user.profile,
            data__gte=hoje
        ).order_by('data', 'horario')
        
        if agendamentos_futuros.exists():
            proximo_agendamento = agendamentos_futuros.first()
        
        # Último agendamento (passado)
        agendamentos_passados = Agendamento.objects.filter(
            cliente=request.user.profile,
            data__lt=hoje
        ).order_by('-data', '-horario')
        
        if agendamentos_passados.exists():
            ultimo_agendamento = agendamentos_passados.first()
        
        # Total de agendamentos
        total_agendamentos = Agendamento.objects.filter(
            cliente=request.user.profile
        ).count()
    
    context = {
        'proximo_agendamento': proximo_agendamento,
        'ultimo_agendamento': ultimo_agendamento,
        'total_agendamentos': total_agendamentos
    }
    
    return render(request, 'usuarios/dashboard.html', context)
