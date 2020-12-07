from django.shortcuts import render

def index (request):
    context = {
        'title': 'Ты в начале пути',
    }
    return render(request, 'mainapp/index.html', context)

def products (request):
    context = {
        'title': 'Эти вещи для тебя',
    }
    return render(request, 'mainapp/products.html', context)


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
