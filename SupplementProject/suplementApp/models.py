from django.db import models

# Create your models here.


class Supplement(models.Model):
    CATEGORIES = [
        ("pro", "Proteins"),
        ("vit", "vitamins"),
        ("cre", "creatines"),
        ("amino", "amino acids"),
        ("pre", "pre-workout")
    ]
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='supplements/')
    code = models.CharField(max_length=30)
    available = models.BooleanField(default=True)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=30)
    category = models.CharField(max_length=6, choices=CATEGORIES)
    description = models.TextField()
