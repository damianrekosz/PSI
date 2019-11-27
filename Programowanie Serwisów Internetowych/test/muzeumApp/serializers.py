from rest_framework import serializers
from .models import Pracownicy
from .models import Eksponaty
from .models import Sale
from .models import Wydarzenia


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

    class Meta:
        model = Wydarzenia
        fields = '__all__'