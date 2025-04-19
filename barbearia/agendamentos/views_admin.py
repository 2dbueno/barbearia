from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from usuarios.models import Profile
from .models import Agendamento
from usuarios.decorators import admin_required

@admin_required
def admin_clientes(request):
    """View para o admin gerenciar clientes"""
    query = request.GET.get('q', '')
    if query:
        clientes = Profile.objects.filter(
            Q(user__first_name__icontains=query) | 
            Q(user__last_name__icontains=query) | 
            Q(cpf__icontains=query) | 
            Q(telefone__icontains=query) |
            Q(user__email__icontains=query)
        ).order_by('user__first_name')
    else:
        clientes = Profile.objects.all().order_by('user__first_name')
    
    # Paginação
    paginator = Paginator(clientes, 10)  # 10 clientes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'agendamentos/admin_clientes.html', {'clientes': page_obj})

@admin_required
def admin_cliente_historico(request, cliente_id):
    """View para o admin visualizar histórico de agendamentos de um cliente"""
    cliente = get_object_or_404(Profile, id=cliente_id)
    agendamentos = Agendamento.objects.filter(cliente=cliente).order_by('-data', '-horario')
    
    return render(request, 'agendamentos/admin_cliente_historico.html', {
        'cliente': cliente,
        'agendamentos': agendamentos
    })
