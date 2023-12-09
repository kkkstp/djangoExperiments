from django import forms
from .models import EquipmentNet


class AddEquipment(forms.ModelForm):
    class Meta:
        model = EquipmentNet
        fields = ['title', 'slug', 'descr', 'state', 'type']