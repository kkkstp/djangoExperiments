from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Equipment

menu = [{'title': 'Navigation', 'url_name': 'index'},
        {'title': 'Equipment', 'url_name': 'equipment'},
        ]

equip = Equipment.objects.all()

def index(request):
   data = {
       'title': menu[0]['title'],
       'menu': menu,
       'url_name': menu[0]['url_name'],
    }
   return render(request, 'firstapp/index.html', context=data)

def equipment(request):
   data = {
       'title': menu[1]['title'],
       'url_name': menu[1]['url_name'],
       'menu': menu,
       'equip': equip,
    }
   return render(request, 'firstapp/equipment.html', context=data)