from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone', 'data_cadastro')
    search_fields = ('user__username', 'user__email', 'cpf', 'telefone')
    list_filter = ('data_cadastro',)
    readonly_fields = ('data_cadastro',)
