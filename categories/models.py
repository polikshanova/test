from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    model of category for spending
    """
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'


class Transaction(models.Model):
    """
    model of user transactions
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    time = models.TimeField()
    organization = models.CharField(max_length=50)
    description = models.TextField(max_length=150, blank=True, null=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Транзакция категории "{self.category}" от даты {self.date}'

    class Meta:
        verbose_name = "Транзкция"
        verbose_name_plural = 'Транзакции'
