from django.db import models
from django.urls import reverse

class Men(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    slug = models.SlugField(db_index=True, unique=True, blank=True)
    prof = models.ForeignKey('Professions', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_person', kwargs={'k_slug': self.slug})

class Professions(models.Model):
    title = models.CharField(max_length=100)
    relevance = models.BooleanField()
    slug = models.SlugField(db_index=True, unique=True, blank=True, default='')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_professions', kwargs={'name_slug': self.slug})

