from django.db import models
from django.conf import settings

# Create your models here.


class Offer(models.Model):

    PERSONAL = 'osobowy'
    MOTORCYCLE = 'motocykl'
    TRUCK = 'ciezarowy'
    PETROL = 'pb'
    DIESEL = 'on'
    LPG = 'lpg'

    kategoria_choices = [
        (PERSONAL, 'Osobowy'),
        (MOTORCYCLE, 'Motocykl'),
        (TRUCK, 'Ciężarowy'),
    ]

    paliwo_choices = [
        (PETROL, 'Benzyna'),
        (DIESEL, 'Diesel'),
        (LPG, 'LPG'),
    ]

    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.CharField(max_length=16, choices=kategoria_choices, default=PERSONAL)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    production_year = models.IntegerField()
    mileage = models.IntegerField()
    capacity = models.IntegerField()
    power = models.IntegerField()
    fuel = models.CharField(max_length=8, choices=paliwo_choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='images/')
    add_date = models.DateField()
    pub_date = models.DateField(null=True, blank=True)
    is_publicated = models.BooleanField(default=False)

    def __str__(self):
        return self.title
