from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    """Verifica se o usuário é um administrador (staff)"""
    return user.is_staff

def admin_required(function=None):
    """Decorator para verificar se o usuário é administrador"""
    actual_decorator = user_passes_test(
        lambda u: u.is_staff,
        login_url='login'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
