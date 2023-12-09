from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('searching_equipment/', views.searching_equipment, name='searching_equipment'),
    #path('addequip/', views.addequip, name='addequip'),
]