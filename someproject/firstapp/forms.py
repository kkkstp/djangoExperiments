from django import forms

class AddPerson(forms.Form):
    name = forms.CharField(max_length=100)
    second_name = forms.CharField(max_length=100)