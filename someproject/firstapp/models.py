from django.db import models
from django.urls import reverse

class EquipmentNet(models.Model):

    class State(models.IntegerChoices):
        OFF = 0, "Off"
        ON = 1, "On"

    class Type(models.TextChoices):
        SWITCH = "sw", "switch"
        ROUTER = "r", "router"
        CAMERA = "cam", "camera"
        UNKNOW = "un", "unknown"

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(db_index=True, unique=True, blank=True)
    descr = models.CharField(max_length=100, blank=True, default='...', verbose_name="Описание")
    state = models.BooleanField(choices=State.choices, default=0, verbose_name="Состояние")
    type = models.CharField(choices=Type.choices, default=Type.UNKNOW, max_length=6, verbose_name="Тип оборудования")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('show_person', kwargs={'slug': self.slug})

class EquipmentForUsers(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(db_index=True, unique=True, blank=True)
    descr = models.CharField(max_length=100, blank=True, default='...', verbose_name="Описание")
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('***', kwargs={'slug': self.slug})
class Workers(models.Model):

    name_and_initials = models.CharField(max_length=100, verbose_name='Имя')
    department = models.CharField(max_length=100, verbose_name='Отдел')
    number = models.IntegerField(verbose_name='Номер телефона')
    slug = models.SlugField(db_index=True, unique=True, blank=True)
    descr = models.CharField(max_length=100, blank=True, default='...', verbose_name="Заметки")
    equip_on_worker = models.ForeignKey("EquipmentForUsers", models.SET_NULL, null=True)

    def __str__(self):
        return self.name_and_initials

    # def get_absolute_url(self):
    #     return reverse('***', kwargs={'slug': self.slug})
