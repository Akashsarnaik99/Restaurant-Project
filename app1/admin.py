from django.contrib import admin

from app1.models import fooditem
from app1.models import Order

# Register your models here.

class fooditemclass(admin.ModelAdmin):
    list_display=('title', 'price', 'rating', 'image','category')
admin.site.register(fooditem,fooditemclass)

class orderclass(admin.ModelAdmin):
    list_display=('customer_name','email','address','pincode','order_detail','payment_mode')
admin.site.register(Order,orderclass)