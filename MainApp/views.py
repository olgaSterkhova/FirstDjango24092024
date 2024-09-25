from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
# Нужный тип исключения для функции get_item()
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

items = Item.objects.all()

def home(request):
    context = {
        "name": "Протасова Ольга Максимовна",
        "email": "OMSterkhova@gmail.com"
    }
    return render(request, 'index.html', context)


def about(request):
    author = {
        "name": "Ольга",
        "middle_name": "Максимовна",
        "last_name": "Протасова",
        "phone": "8-953-916-16-10",
        "email": "OMSterkhova@gmail.com",
        "bdate":"6 января"
    }
    text = f"""
        <header>
        / <a href="/"> Home </a> / <a href="/items"> Items</a> / <a href="/about"> About </a>
        </header>
        <h2> Информация об авторе </h2>
        Имя: <b>{author['name']}</b><br>
        Отчество: <b>{author['middle_name']}</b><br>
        Фамилия: <b>{author['last_name']}</b><br>
        Телефон: <b>{author['phone']}</b><br>
        Email: <b>{author['email']}</b><br>
    """
    return HttpResponse(text)


def get_item(request, item_id: int):
    """ Функция по item_id нужного элемента вернет имя и кол-во. """
    for item in items:
        if item["id"] == item_id:
            context = {"item": item}
            return render(request, "item_page.html", context)
    # Если элемент не найден - нужно вернуть соотвествующий ответ(response)
    return HttpResponseNotFound(f"Item with id={item_id} not found.")


def get_items(request):
    context = {"items": items}
    return render(request, "items_list.html", context)

#def get_items(request):
 #   context = {"items": items}
 #   return render(request, "items_list.html", context)

