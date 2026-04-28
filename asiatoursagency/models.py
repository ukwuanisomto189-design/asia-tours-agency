from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.origin_country} to {self.destination_country}"


class Hotel(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    price_per_night = models.IntegerField()