from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Men, Professions

menu = [{'title': 'Main page', 'url_name': 'index'},
        {'title': 'Table', 'url_name': 'table'},
        {'title': 'Contacts', 'url_name': 'show_contacts'},
        {'title': 'About', 'url_name': 'show_about'}
]

linksOfProfession = Professions.objects.all()
Men = Men.objects.all()

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
        'links': linksOfProfession,
        'Men': Men,
    }
    return render(request, 'firstapp/table.html', context=data)

def show_professions(request, name_slug):
    title, url_name = "а че", menu[2]['url_name']
    linksOfProfession = Men.objects.filter(slug='name_slug')
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
        'links': linksOfProfession,
        'Men': Men,
    }

    return render(request, 'firstapp/professions.html', context=data)

def show_contacts(request):
    title, url_name = menu[2]['title'], menu[2]['url_name']
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
    }
    return render(request, 'firstapp/show_about.html', context=data)

def show_about(request):
    title, url_name = menu[3]['title'], menu[3]['url_name']
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
    }
    return render(request, 'firstapp/show_about.html', context=data)

def show_person(request, k_slug):
    men = get_object_or_404(Men, slug=k_slug)
    title, url_name = menu[1]['title'], menu[1]['url_name']
    data = {
        'title': title,
        'menu': menu,
        'url_name': url_name,
    }
    return render(request, 'firstapp/show_person.html', context=data)