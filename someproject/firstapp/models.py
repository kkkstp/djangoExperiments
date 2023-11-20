from django.db import models
from django.urls import reverse

class Men(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()