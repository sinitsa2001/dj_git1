from django.shortcuts import render
from mainapp.models import Product,ProductCategory

def index (request):
    context = {
        'title': 'Ты в начале пути',
    }
    return render(request, 'mainapp/index.html', context)

def products (request, pk =None):
    context = {
        'title': 'Эти вещи для тебя',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all(),
        # 'products': [
        #     { 'name':'Худи черного цвета с монограммами adidas Originals', 'price':'6 090,00 руб.'},
        #     {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.'},
        #     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.'},
        #     {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.'},
        #     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.'},
        #     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.'},
        # ]
    }
    return render(request, 'mainapp/products.html', context = context)

# def categories (request):
#     context ={
#         'category': ProductCategory.objects.all()
#     }
#     return render(request, 'mainapp/products.html', context)

# def categories (request):
#
#     return render(request, 'mainapp/products.html', context=context)


def test_context (request):
    context ={
        'title':'добро пожаловать',
        'username':'Lele Sinitsyna',
        'products': [
            {'name':'Черное худи', 'price': '12000 usd'},
            {'name': 'Белое разное', 'price': '2000 usd'},
        ],
        # 'promotion':True,
        'promotion_products':[
            {'name': 'Тухольки', 'price': 'Дешевле грибов'},
        ]

    }
# products= context['products']
    return render(request, 'mainapp/context.html',context)
