from django.contrib.auth import forms as fm
from django import forms
from django.contrib.auth.models import User


class LoginForm(fm.AuthenticationForm):
    username = fm.UsernameField(label='用户名',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入3-20位用户名'}))
    password = forms.CharField(
        label='密码',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}),
    )


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入3-20位用户名'}))
    email = forms.EmailField(label='邮箱',
                             required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱,可以为空'}))
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}),
    )
    password_again = forms.CharField(
        label='重复密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_again']

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次密码不一致')
        return password_again

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已经存在')
        return username
