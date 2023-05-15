from django.contrib.auth.models import User
from django.db import models


class SickList(models.Model):
    class Meta:
        verbose_name = 'Больничный'
        verbose_name_plural = 'Больничные'
    LIST_TYPE=(
        ('kid', 'По уходу за ребенком'),
        ('ill', 'В связи с болезнью'),
        ('pregnancy', 'По беременности и родам'),
        ('other', 'Другое'),
    )
    amount = models.IntegerField('Процент начисления')
    base_pay = models.DecimalField('Тарифная ставка', max_digits=8, decimal_places=2)
    start_date = models.DateField('Дата начала больничного')
    end_date = models.DateField('Дата окончания больничного', blank=True, null=True)
    total = models.DecimalField('Размер выплаты', max_digits=8, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=25, choices=LIST_TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
