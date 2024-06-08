from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products/')
    price=models.IntegerField()
    quantity=models.IntegerField()

class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    def str(self):
        return f"{self.name} {self.surname}"

class Order(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

