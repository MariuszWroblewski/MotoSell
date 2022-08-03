from django.db import models
from django.conf import settings

# Create your models here.


class Oferta(models.Model):

    OSOBOWY = 'osobowy'
    MOTOCYKL = 'motocykl'
    CIEZAROWY = 'ciezarowy'
    BENZYNA = 'pb'
    DIESEL = 'on'
    LPG = 'lpg'

    kategoria_choices = [
        (OSOBOWY, 'Osobowy'),
        (MOTOCYKL, 'Motocykl'),
        (CIEZAROWY, 'Ciężarowy'),
    ]

    paliwo_choices = [
        (BENZYNA, 'Benzyna'),
        (DIESEL, 'Diesel'),
        (LPG, 'LPG'),
    ]

    tytul = models.CharField(max_length=64)
    opis = models.CharField(max_length=512)
    kategoria = models.CharField(max_length=16, choices=kategoria_choices, default=OSOBOWY)
    marka = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    rok_produkcji = models.IntegerField()
    przebieg = models.IntegerField()
    pojemnosc_skokowa = models.IntegerField()
    moc = models.IntegerField()
    paliwo = models.CharField(max_length=8, choices=paliwo_choices)
    uzytkownik = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zdjecie = models.ImageField(null=True)
    data_dodania = models.DateField()
    data_publikacji = models.DateField(null=True)
