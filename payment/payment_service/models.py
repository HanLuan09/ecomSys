from django.db import models

class PaymentMethod(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    
class Payment(models.Model):
    order_id = models.IntegerField()
    date_paymented = models.DateField(auto_now_add=True)
    total = models.FloatField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    status = models.BooleanField()