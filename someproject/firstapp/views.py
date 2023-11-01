from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import MainDB


def base(request):
    posts = MainDB.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'firstapp/mainpage.html', context=data)

def show_table(request, post_slug):
    post = get_object_or_404(MainDB, slug=post_slug)
    data = {
        'post': post,
        }
    return render(request, 'firstapp/tableDB.html', context=data)