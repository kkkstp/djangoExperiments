from django.shortcuts import render
<<<<<<< HEAD
from .models import EquipmentNet, Workers, EquipmentForUsers
from .forms import AddEquipment

menu = [{'title': 'Navigation', 'url_name': 'index'},
        {'title': 'Searching equipment', 'url_name': 'searching_equipment'},
=======
from .models import Equipment
from .forms import AddEquipment

menu = [{'title': 'Navigation', 'url_name': 'index'},
        {'title': 'Equipment', 'url_name': 'equipment'},
>>>>>>> 25021bcecee43a0182eaae73747d90fea5dccdf3
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
<<<<<<< HEAD
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
=======
   return render(request, 'firstapp/equipment.html', context=data)

def addequip(request):
    form = AddEquipment()
    data = {
       'title': menu[2]['title'],
       'url_name': menu[2]['url_name'],
       'menu': menu,
       'form': form,
    }
    return render(request, 'firstapp/addequip.html', context=data)
>>>>>>> 25021bcecee43a0182eaae73747d90fea5dccdf3
