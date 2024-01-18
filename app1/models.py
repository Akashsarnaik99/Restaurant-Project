from django.db import models


# Create your models here.

# items in Menu

class fooditem(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField(max_length=50)
    rating=models.FloatField(max_length=5)
    image = models.ImageField(upload_to='covers/', blank=True)
    category= models.CharField(max_length=100)

# for place order details

class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    pincode=models.IntegerField(max_length=100)
    order_detail=models.TextField(max_length=100)
    payment_mode=models.CharField(max_length=50)

   

    


# def __str__(self):
#     return str(self.title) + "["+str(self.rating)+']'