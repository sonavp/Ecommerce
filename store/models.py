from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    description=models.TextField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to='images',null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to='images',null=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.IntegerField(null=False)
    selling_price=models.IntegerField(null=False)
    description=models.TextField(max_length=300,null=False)
    
    def __str__(self):
        return self.name
    

class cart(models.Model):
    item=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField(null=False,default=1)
    date=models.DateTimeField(auto_now_add=True)
    
class order(models.Model):
    order_item=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    order_status=models.BooleanField(null=True,default="pending")
    address=models.TextField(null=False)
    price=models.IntegerField(null=True)