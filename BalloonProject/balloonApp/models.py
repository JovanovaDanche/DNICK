from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Balloon(models.Model):
    typeballoon = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    capacity = models.IntegerField()


class Airline(models.Model):
    name = models.CharField(max_length=15)
    typeballoon = models.CharField(max_length=15)
    estYear = models.IntegerField()
    out_of_Europe = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Pilot(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    yearofbirth = models.IntegerField()
    hoursflying = models.IntegerField()
    title = models.CharField(max_length=15)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def str(self):
        return f"{self.firstname} {self.lastname}"


class Flight(models.Model):
    code = models.CharField(max_length=10)
    airportBegin = models.CharField(max_length=15)
    airportEnd = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cover_images/")
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)


class PilotsAirline(models.Model):
    airlines = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilots = models.ManyToManyField(Pilot)
