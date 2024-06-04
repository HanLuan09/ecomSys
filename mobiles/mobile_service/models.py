from djongo import models

class Category(models.Model):
    category_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)

    def __str__(self):
        return self.name

class Producer(models.Model):
    producer_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)

    def __str__(self):
        return self.name


class Mobile(models.Model):
    mobile_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)
    #image = models.ImageField(upload_to='image/')
    image = models.CharField(max_length=255)
    price = models.FloatField()
    sale = models.FloatField()
    quantity = models.IntegerField()
    type = models.CharField(max_length=50, default = "mobile")
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name