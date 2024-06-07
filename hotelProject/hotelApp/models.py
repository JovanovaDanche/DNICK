# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Employee(models.Model):
    TYPE_CHOICES = [
        ('H', 'higienichar'),
        ('R', 'recepcioner'),
        ('M', 'menadzer'),
    ]
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    description = models.TextField()
    emp_year = models.IntegerField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    def __str__(self):
        return self.name


class Room(models.Model):
    num = models.IntegerField()
    num_beds = models.IntegerField()
    balcony = models.BooleanField(default=False)
    is_clean = models.BooleanField(default=False)
    employees = models.ManyToManyField(Employee, through='RoomEmployee')

    def str(self):
        return f"{self.num} {self.is_clean}"


class Reservation(models.Model):
    code = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reservations/')
    confirmed = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def str(self):
        return f"{self.code} {self.room}"


class RoomEmployee(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
