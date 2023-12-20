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

def adding_person_done(request):
   name, second_name, content = request.POST['name'], request.POST['second_name'], request.POST['content']
   data = {
      'name': name,
      'second_name': second_name,
      'content': content
   }
   print(request.POST)
   new_one = SomeDB.objects.create(name=name, second_name=second_name, content=content)
   return render(request, 'firstapp/adding_person_done.html', context=data)
