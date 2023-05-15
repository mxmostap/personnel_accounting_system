from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    phone = models.CharField('Номер телефона', max_length=13)
    birth_date = models.DateField('Дата рождения')
    salary = models.DecimalField('Оклад', max_digits=8, decimal_places=2, default=0)
    employment_date = models.DateField('Дата устройства на работу')
    dismissal_date = models.DateField('Дата увольнения', blank=True, null=True)
    picture = models.ImageField(upload_to='media', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)