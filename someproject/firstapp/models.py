from django.db import models
from django.urls import reverse

class SomeDB(models.Model):

    name = models.CharField(max_length=100, default='...', verbose_name='Имя')
    second_name = models.CharField(max_length=100, default='...', verbose_name='Фамилия')

    def __str__(self):
        return self.name