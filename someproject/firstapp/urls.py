from django.urls import path
from firstapp import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('table/', views.table, name='table'),
    path('professions/', views.show_professions, name='show_professions'),
    path('contacts/', views.show_contacts, name='show_contacts'),
    path('about/', views.show_about, name='show_about'),
    path('men/<slug:k_slug>/', views.show_person, name='show_person'),
]