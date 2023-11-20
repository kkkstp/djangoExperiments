from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

menu = [{'title': "Main page", 'url_name': 'mainpage'},
        {'title': "Add person", 'url_name': 'add_person'},
        {'title': "Contacts", 'url_name': 'contact'},
        {'title': "About", 'url_name': 'about'}
]
def index(request):
    data = {
        'title': 'Main page',
        'menu': menu,
    }
    return render(request, 'firstapp/index.html')