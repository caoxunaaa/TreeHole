from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm


class Login(LoginView):
    template_name = 'user/login.html'
    form_class = LoginForm


class Logout(LogoutView):
    pass


