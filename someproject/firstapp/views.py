from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Men, Professions

menu = [{'title': 'Main page', 'url_name': 'index'},
        {'title': 'Table', 'url_name': 'table'},
        {'title': 'Contacts', 'url_name': 'show_contacts'},
        {'title': 'About', 'url_name': 'show_about'}
]

def index(request):
    title, url_name = 'Main page', 'index'
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
    }
    return render(request, 'firstapp/index.html', context=data)
