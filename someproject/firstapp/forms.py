from django import forms
from .models import Equipment


class AddEquipment(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['title', 'slug', 'descr', 'state', 'type']