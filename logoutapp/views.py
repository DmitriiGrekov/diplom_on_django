from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def logout_view(request):
    """
    Функция выхода пользователя из аккаунта
    """
    logout(request)
    return HttpResponseRedirect("/login")
