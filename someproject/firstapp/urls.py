from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_person/', views.add_person, name='add_person'),
    path('adding_person_done/', views.adding_person_done, name='adding_person_done'),
]