from django.db import models

class OrderItem(models.Model):
    quantity = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.FloatField()
    sale = models.FloatField()
    product_id = models.CharField(max_length=7)

class Order(models.Model):
    user_id = models.CharField(max_length=7)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    status = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)
    order_items = models.ManyToManyField(OrderItem)