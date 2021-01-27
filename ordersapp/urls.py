from django.urls import path

import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
   path('', ordersapp.OrderList.as_view(), name='orders'),



    # path('<int:category_id>/', mainapp.products, name = 'product'),
    # path('page/<int:page>/', mainapp.products, name = 'page'),
]

