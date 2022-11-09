from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    model of users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
