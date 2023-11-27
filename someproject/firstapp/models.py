from django.db import models
from django.urls import reverse

class Men(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    second_name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(db_index=True, unique=True, blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('men', kwargs={'slug': self.slug})
