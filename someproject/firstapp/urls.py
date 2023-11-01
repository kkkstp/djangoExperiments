from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.base, name='base'),
    path('post/<slug:post_slug>', views.show_table, name='post'),
]