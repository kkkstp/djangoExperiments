from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

menu = [{'title': 'Main page', 'url_name': 'index'},
        {'title': 'Table', 'url_name': 'table'},
        {'title': 'Contacts', 'url_name': 'show_contacts'},
        {'title': 'About', 'url_name': 'show_about'}
]
def index(request):
    title, url_name = menu[0]['title'], menu[0]['url_name']
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
    }
    return render(request, 'firstapp/index.html', context=data)

def table(request):
    title, url_name = menu[1]['title'], menu[1]['url_name']
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
    }
    return render(request, 'firstapp/table.html', context=data)

def show_contacts(request):
    title, url_name = menu[2]['title'], menu[2]['url_name']
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
    }
    return render(request, 'firstapp/show_contacts.html', context=data)

def show_about(request):
    title, url_name = menu[3]['title'], menu[3]['url_name']
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
    }
    return render(request, 'firstapp/show_about.html', context=data)