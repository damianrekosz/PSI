from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pracownicy, Eksponaty, Sale, Wydarzenia
from .serializers import PracownicySerializer, EksponatySerializer, SaleSerializer, WydarzeniaSerializer
from rest_framework.parsers import JSONParser
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('muzeumApp/index.html')
    return HttpResponse(template.render(request))


class PracownicyLista(APIView):

    def get(self, request):
        prac = Pracownicy.objects.all()
        serializer = PracownicySerializer(prac, many = True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        dane = JSONParser().parse(request)
        serializer = PracownicySerializer(data = dane)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


class EksponatyLista(APIView):

    def get(self, request):
        prac = Eksponaty.objects.all()
        serializer = EksponatySerializer(prac, many = True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        dane = JSONParser().parse(request)
        serializer = EksponatySerializer(data=dane)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SaleLista(APIView):

    def get(self, request):
        prac = Sale.objects.all()
        serializer = SaleSerializer(prac, many = True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        dane = JSONParser().parse(request)
        serializer = SaleSerializer(data=dane)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class WydarzeniaLista(APIView):

    def get(self, request):
        prac = Wydarzenia.objects.all()
        serializer = WydarzeniaSerializer(prac, many = True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        dane = JSONParser().parse(request)
        serializer = WydarzeniaSerializer(data=dane)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
