#from django.shortcuts import render

# Create your views here
#<h1>"Изучаем django"</h1><strong>Автор</strong>: <i>Иванов И.П.</i>
author=(
   "" имя: Иван
    отчество: Иванович
    Фамилия: Иванов
    телефон:55-42-50
)
from django.http import HttpResponse


def about(request):
    text = f'''
Имя:<b>(author["Имя"])</b>
'''
    return HttpResponse(text)

