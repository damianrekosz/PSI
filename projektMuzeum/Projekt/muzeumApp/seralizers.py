from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


class Pracownicy(object):
    def __init__(self, nazwisko, imie, pesel):
        self.nazwisko = nazwisko
        self.imie = imie
        self.pesel = pesel


class PracownicySeralizer(serializers.Serializer):
    nazwisko = serializers.CharField(max_length=200)
    imie = serializers.CharField(max_length=200)
    pesel = serializers.IntegerField()


pracownik = Pracownicy(nazwisko='kowalski', imie='janusz', pesel='12345678911')
PracownikSeralizer = PracownicySeralizer(pracownik)
jsonPracownik = JSONRenderer().render(PracownikSeralizer.data)

stream = io.BytesIO(jsonPracownik)
data = JSONParser().parse(stream)

