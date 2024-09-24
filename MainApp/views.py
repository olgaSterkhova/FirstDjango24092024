#from django.shortcuts import render

# Create your views here
#<h1>"Изучаем django"</h1><strong>Автор</strong>: <i>Иванов И.П.</i>
from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello, World!")

