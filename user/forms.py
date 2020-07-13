from django.contrib.auth import forms as fm
from django import forms


class LoginForm(fm.AuthenticationForm):
    username = fm.UsernameField(label='用户名', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入3-30位用户名'}))
    password = forms.CharField(
        label='密码',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}),
    )

