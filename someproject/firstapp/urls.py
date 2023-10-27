from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.base, name='base'),
]