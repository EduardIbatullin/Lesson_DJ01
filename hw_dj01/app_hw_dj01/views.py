from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, 'app_hw_dj01/index.html')


def data_view(request):
    return HttpResponse('<h1>Страница Data</h1><p>Это страница с данными.</p>')


def test_view(request):
    return HttpResponse('<h1>Страница Test</h1><p>Это тестовая страница.</p>')