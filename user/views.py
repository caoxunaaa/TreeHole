from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse


class Login(LoginView):
    template_name = 'user/login.html'
    form_class = LoginForm


class Logout(LogoutView):
    pass


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = 'login'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data.get('email', '')
        password = form.cleaned_data['password_again']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user = auth.authenticate(username=username, password=password)
        auth.login(self.request, user)
        return redirect(self.request.GET.get('next', reverse('home')))



