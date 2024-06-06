from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    country = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Workshop(models.Model):
    name = models.CharField(max_length=30)
    yearEst = models.IntegerField()
    oldTimer = models.BooleanField(default=False)


class Car(models.Model):
    type = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    maxSpeed = models.IntegerField()
    color = models.CharField(max_length=30)

    def str(self):
        return f"{self.type} {self.maxSpeed}"


class Repair(models.Model):
    code = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cover_images/")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)


class WorkshopManufacturers(models.Model):
    workshops=models.ForeignKey(Workshop, on_delete=models.CASCADE)
    manufacturers=models.ManyToManyField(Manufacturer)
