from django.db import models
from django.contrib import admin

class deliverydatabase(models.Model):
    class Meta():
        permissions = (("view_status", "can view staff details."),
                 ("view_address", "can view customer details"),
        )
    username_primary_key = models.CharField(max_length=30, help_text="User id must be unique", primary_key=True,unique=True)
    address= models.CharField(max_length=30)
    phone_number = models.IntegerField()
    order_name = models.CharField(max_length=20)
    coupon_code = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,unique=True)

class deliveryadmin(admin.ModelAdmin):
    list_display = ('username_primary_key', 'address', 'phone_number', 'order_name','coupon_code','email')
