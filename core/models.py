from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

class User(AbstractUser):
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
