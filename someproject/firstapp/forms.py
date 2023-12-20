from django import forms
from .models import SomeDB
class AddPerson(forms.ModelForm):

    class Meta:
        model = SomeDB
        fields = ['name', 'second_name', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 9})
        }

