from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendar/', views.agendar, name='agendar'),
    path('cancelar/<int:agendamento_id>/', views.cancelar_agendamento, name='cancelar_agendamento'),
    path('admin/agendamentos/', views.admin_agendamentos, name='admin_agendamentos'),
    path('admin/agendamentos/dia/', views.admin_agendamentos_dia, name='admin_agendamentos_dia'),
    path('admin/agendamentos/semana/', views.admin_agendamentos_semana, name='admin_agendamentos_semana'),
    path('admin/agendamentos/mes/', views.admin_agendamentos_mes, name='admin_agendamentos_mes'),
    path('admin/agendar/<str:cpf>/', views.admin_agendar, name='admin_agendar'),
]
