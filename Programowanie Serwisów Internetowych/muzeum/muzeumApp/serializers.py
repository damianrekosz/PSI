from rest_framework import serializers
from .models import Pracownicy
from .models import Eksponaty
from .models import Sale
from .models import Wydarzenia
from django.contrib.auth.models import User


class PracownicySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pracownicy
        #fields = ('nazwisko', 'imie', 'pesel')
        fields = '__all__'


class EksponatySerializer(serializers.ModelSerializer):

    class Meta:
        model = Eksponaty
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = '__all__'


class WydarzeniaSerializer(serializers.ModelSerializer):
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')

    class Meta:
        model = Wydarzenia
        fields = '__all__'


class WlascicielSerializer(serializers.ModelSerializer):
    wydarzenia = serializers.PrimaryKeyRelatedField(many=True, queryset=Wydarzenia.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'wydarzenia', 'date_joined', 'groups']
