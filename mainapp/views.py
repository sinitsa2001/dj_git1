from django.shortcuts import render

def index (request):
    return render(request, 'mainapp/index.html')

def products (request):
    return render(request, 'mainapp/products.html')


def test_context (request):
    context ={
        'title':'добро пожаловать',
        'username':'Lele Sinitsyna',
        'products': [
            {'name':'Черное худи', 'price': '12000 usd'},
            {'name': 'Белое разное', 'price': '2000 usd'},
        ],
        'promotion':True,
        'promotion_products':[
            {'name': 'Тухольки', 'price': 'шара'},
        ]

    }

    return render(request, 'mainapp/context.html',context)
