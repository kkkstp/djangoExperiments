from django.shortcuts import render

from .forms import AddPerson
from .models import SomeDB


def index(request):
   somedb = SomeDB.objects.all()
   data = {'somedb': somedb}
   return render(request, 'firstapp/index.html', context=data)

def add_person(request):
   form = AddPerson()
   data = {'form': form}
   return render(request, 'firstapp/add_person.html', context=data)