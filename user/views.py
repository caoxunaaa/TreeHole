from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class Login(LoginView):
    template_name = 'user/login.html'
    form_class = LoginForm

    def get_success_url(self):
        if '?next=' not in self.request.GET.get('next', ''):
            return self.request.GET.get('next', reverse('home'))
        else:
            return reverse('home')


class Logout(LogoutView):
    pass


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'user/register.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data.get('email', '')
        password = form.cleaned_data['password_again']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user = auth.authenticate(username=username, password=password)
        auth.login(self.request, user)
        if '?next=' not in self.request.GET.get('next', ''):
            return redirect(self.request.GET.get('next', reverse('home')))
        else:
            return redirect(reverse('home'))


