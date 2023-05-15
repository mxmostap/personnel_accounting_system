from django.contrib.auth.models import User
from django.db import models

class Salary(models.Model):
    class Meta:
        verbose_name = 'Заработная плата'
        verbose_name_plural = 'ЗП'
    reward = models.IntegerField('Размер премии',  blank=True, null=True)
    payment_date = models.DateField('Дата выплаты')
    total = models.DecimalField('Итоговая сумма', max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
