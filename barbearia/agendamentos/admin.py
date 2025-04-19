from django.contrib import admin
from .models import Barbeiro, Servico, Agendamento

@admin.register(Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    search_fields = ('nome',)
    list_filter = ('ativo',)

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'preco', 'duracao')
    search_fields = ('tipo', 'descricao')
    list_filter = ('tipo',)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'barbeiro', 'servico', 'data', 'horario', 'data_agendamento')
    search_fields = ('cliente__user__username', 'cliente__cpf', 'barbeiro__nome')
    list_filter = ('data', 'barbeiro', 'servico')
    readonly_fields = ('data_agendamento',)
