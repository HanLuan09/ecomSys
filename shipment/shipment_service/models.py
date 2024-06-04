from django.db import models

class ShipmentInfo(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=200) 
    is_active = models.BooleanField(default=True)

class Transaction(models.Model):
    name = models.CharField(max_length=50)
    coefficient = models.FloatField()
    is_active = models.BooleanField(default=True)
    des = models.CharField(max_length=250)

class Carriers(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    des = models.CharField(max_length=250)

class Shipment(models.Model):
    order_id =  models.IntegerField()
    shipment_status = models.CharField(max_length=20)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=15)
    shipment_info = models.ForeignKey(ShipmentInfo, on_delete=models.CASCADE)
    carrier = models.ForeignKey(Carriers, on_delete=models.CASCADE)
    
