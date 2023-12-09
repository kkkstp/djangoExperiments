from django import forms
<<<<<<< HEAD
from .models import EquipmentNet
=======
from .models import Equipment
>>>>>>> 25021bcecee43a0182eaae73747d90fea5dccdf3


class AddEquipment(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = EquipmentNet
=======
        model = Equipment
>>>>>>> 25021bcecee43a0182eaae73747d90fea5dccdf3
        fields = ['title', 'slug', 'descr', 'state', 'type']