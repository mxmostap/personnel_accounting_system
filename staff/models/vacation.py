from django.contrib.auth.models import User
from django.db import models


class Vacation(models.Model):
    class Meta:
        verbose_name = 'Отпуск'
        verbose_name_plural = 'Отпуска'
    start_date = models.DateField('Дата начала отпуска')
    end_date = models.DateField('Дата окончания отпуска')
    total = models.DecimalField('Размер выплаты', max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
