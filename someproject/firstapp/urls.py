from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('searching_equipment/', views.searching_equipment, name='searching_equipment'),
    #path('addequip/', views.addequip, name='addequip'),
=======
    path('equipment/', views.equipment, name='equipment'),
    path('addequip/', views.addequip, name='addequip'),
>>>>>>> 25021bcecee43a0182eaae73747d90fea5dccdf3
]