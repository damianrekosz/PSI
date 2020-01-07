from django.db import models


class Pracownicy(models.Model):
    nazwisko = models.CharField(max_length=200)
    imie = models.CharField(max_length=200)
    pesel = models.IntegerField()


class Eksponaty(models.Model):
    nazwa = models.CharField(max_length=200)
    dataProdukcji = models.DateField()
    miejscePochodzenia = models.CharField(max_length=200)
    stanEksponatu = models.CharField(max_length=200)
    czyZarezerwowany = models.BooleanField()


class Sale(models.Model):
    rozmiar = models.IntegerField()


class Wydarzenia(models.Model):
    pracownicy = models.ForeignKey(Pracownicy, on_delete=models.CASCADE)
    eksponaty = models.ForeignKey(Eksponaty, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=200)
    wlasciciel = models.ForeignKey('auth.User', related_name='wydarzenia', on_delete=models.CASCADE)
