from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib import auth

class Login(View):
    def get(self, request):
        context = dict()
        loginform = LoginForm()
        context['form'] = loginform
        return render(request, 'user/login.html', context)

    def post(self, request):
        loginform = LoginForm(request.POST)
        auth.login(request, user)

# class Register(CreateView):
#     pass
