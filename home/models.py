from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CATEGORY_CHOICE=(
    ('Apple','Apple'),
    ('Samsung','Samsung'),
    ('Redmi','Redmi'),
    ('Oneplus','Oneplus'),
    ('Realme','Realme')
)


class Product(models.Model):
    product_name=models.CharField(max_length=200, null=True)
    product_image=models.ImageField(null=True, blank=True)
    brand=models.CharField(choices=CATEGORY_CHOICE,max_length=100,null=True)
    actual_price=models.IntegerField(null=True)
    available_item=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.product_name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    product_name = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return self.product_name.product_name