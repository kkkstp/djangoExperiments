from django.shortcuts import render
from .models import EquipmentNet, Workers, EquipmentForUsers
from .forms import AddEquipment

menu = [{'title': 'Navigation', 'url_name': 'index'},
        {'title': 'Searching equipment', 'url_name': 'searching_equipment'},
        {'title': 'Adding equipment', 'url_name': 'addequip'},
        ]

def index(request):
   data = {
       'title': menu[0]['title'],
       'menu': menu,
       'url_name': menu[0]['url_name'],
    }
   return render(request, 'firstapp/index.html', context=data)

def searching_equipment(request):
   workers = Workers.objects.all()
   equip = EquipmentForUsers.objects.all()
   data = {
       'title': menu[1]['title'],
       'url_name': menu[1]['url_name'],
       'menu': menu,
       'equip': equip,
    }
   return render(request, 'firstapp/searching_equipment.html', context=data)

# def addequip(request):
#     form = AddEquipment()
#     data = {
#        'title': menu[2]['title'],
#        'url_name': menu[2]['url_name'],
#        'menu': menu,
#        'form': form,
#     }
#     return render(request, 'firstapp/addequip.html', context=data)