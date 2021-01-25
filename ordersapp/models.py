from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEED = 'PRD'
    PAID = 'PD'
    READY = 'PDY'
    DONE = 'DN'
    CANCEL = 'CNC'

    ORDER_STATUSES =(
        (FORMING,'формируется'),
        (SENT_TO_PROCEED,'отправлен на обработку'),
        (PROCEED, 'обработан'),
        (PAID, 'оплачен'),
        (READY, 'готов к выдаче'),
        (DONE, 'выдан'),
        (CANCEL,'отменен'),
    )

    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='изменен')

    status = models.CharField(
        verbose_name='статус',
        choices= ORDER_STATUSES,
        max_length=3,
        default=FORMING
    )

    is_active = models.BooleanField(default=True, verbose_name='активен')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created_at',)

    def total_quantity(self):
        _items = self.orderitems.select_related()  # baskets =
        _total_quantity = sum(list(map(lambda x: x.quantiny, _items)))
        return _total_quantity

    def total_sum(self):
        _items = self.orderitems.select_related()
        _total_sum = sum(list(map(lambda x: x.quantiny * x.product.price, _items)))
        return _total_sum

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()  # item.quantity

        self.is_active = False
        self.save()



class OrderItem (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')


    def sum (self):
        return self.product.price * self.quantity