from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, upload_to='images/', blank=True)
    add_date = models.DateField(auto_now_add=True,  blank=False, null=False,)
    pub_date = models.DateField(default=None, blank=True, null=True)
    is_pub = models.BooleanField(default=False, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
