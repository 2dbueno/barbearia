from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """Formulário para registro de usuários"""
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True, label='Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome')
    cpf = forms.CharField(max_length=14, required=True, label='CPF')
    telefone = forms.CharField(max_length=15, required=True, label='Telefone')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'cpf', 'telefone', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Atualizar o perfil com CPF e telefone
            user.profile.cpf = self.cleaned_data['cpf']
            user.profile.telefone = self.cleaned_data['telefone']
            user.profile.save()
            
        return user

class UserUpdateForm(forms.ModelForm):
    """Formulário para atualização de dados do usuário"""
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True, label='Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    """Formulário para atualização de dados do perfil"""
    class Meta:
        model = Profile
        fields = ['cpf', 'telefone', 'foto']
