from django.http import HttpResponse
import datetime
import os

from django.urls import reverse


def hello_view(request):
    name = request.GET.get('name', 'User')
    return HttpResponse(f"hello {name}")


def index_view(request):
    stri = 'Вы попали на главную страницу<br>' \
           f'<a href="http://127.0.0.1:8000/current_time/">{reverse("current_time")}</a> - показ текущего времени<br>' \
           f'<a href="http://127.0.0.1:8000/workdir/">{reverse("workdir")}</a> - показ дирректории'
    return HttpResponse(stri)


def current_time_view(request):
    time_now = datetime.datetime.now()
    return HttpResponse(time_now)


def workdir_view(request):
    return HttpResponse(os.getcwd())
