from django.shortcuts import render

def home(request):
    """View para a página inicial do site"""
    return render(request, 'core/home.html')

def sobre(request):
    """View para a página sobre"""
    return render(request, 'core/sobre.html')

def contato(request):
    """View para a página de contato"""
    return render(request, 'core/contato.html')
