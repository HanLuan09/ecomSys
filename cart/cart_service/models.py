from django.db import models

class CartItem(models.Model):
    user_id = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    type = models.CharField(max_length=50)
    product_id = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    