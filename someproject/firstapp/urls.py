from django.urls import path
from firstapp import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_person/', views.add_person, name='add_person'),
    path('contacts/', views.show_contacts, name='show_contacts'),
    path('about/', views.show_about, name='show_about'),
]