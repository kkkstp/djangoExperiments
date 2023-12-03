from django.db import models
from django.urls import reverse

class Equipment(models.Model):
    class State(models.IntegerChoices):
        ON = 0, "On"
        OFFa = 1, "Off"

    title = models.CharField(max_length=100)
    slug = models.SlugField(db_index=True, unique=True, blank=True)
    descr = models.CharField(max_length=100, blank=True)
    state = models.BooleanField(choices=State.choices)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('show_person', kwargs={'slug': self.slug})

