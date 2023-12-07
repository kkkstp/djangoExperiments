from django.db import models
from django.urls import reverse

class Equipment(models.Model):

    class State(models.IntegerChoices):
        OFF = 0, "Off"
        ON = 1, "On"

    class Type(models.TextChoices):
        SWITCH = "sw", "switch"
        ROUTER = "r", "router"
        CAMERA = "cam", "camera"
        UNKNOW = "un", "unknown"

    title = models.CharField(max_length=100)
    slug = models.SlugField(db_index=True, unique=True, blank=True)
    descr = models.CharField(max_length=100, blank=True, default='...')
    state = models.BooleanField(choices=State.choices, default=0)
    type = models.CharField(choices=Type.choices, default=Type.UNKNOW, max_length=6)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('show_person', kwargs={'slug': self.slug})