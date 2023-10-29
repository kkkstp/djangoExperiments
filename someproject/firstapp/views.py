from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import MainDB


def base(request):
    post = MainDB.objects.all()
    #print(post)
    data = {
        'post': post,
    }
    return render(request, 'firstapp/mainpage.html', context=data)

def show_table(request, post_slug):
    post = get_object_or_404(MainDB, pk=post_slug)
    data = {'post': post,
        }
    return render(request, 'firstapp/tableDB.html', context=data)