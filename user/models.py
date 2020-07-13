from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    nickname = models.CharField(max_length=20)


def has_nickname(self):
    return Profile.objects.filter(user=self).exists()


def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists():
        return Profile.objects.get(user=self).nickname
    else:
        return self.username


User.has_nickname = has_nickname
User.get_nickname_or_username = get_nickname_or_username
