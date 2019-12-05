from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import Pracownicy, Eksponaty, Sale, Wydarzenia
from .serializers import PracownicySerializer, EksponatySerializer, SaleSerializer, WydarzeniaSerializer
from rest_framework.parsers import JSONParser
from django.template import loader
from django.contrib.auth.models import User
from .serializers import WlascicielSerializer


# Create your views here.
def index(request):
    template = loader.get_template('muzeumApp/index.html')
    return HttpResponse(template.render({}, request))


class PracownicyLista(APIView):

    def get(self, request):
        prac = Pracownicy.objects.all()
        serializer = PracownicySerializer(prac, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PracownicySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EksponatyLista(APIView):

    def get(self, request):
        prac = Eksponaty.objects.all()
        serializer = EksponatySerializer(prac, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EksponatySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleLista(APIView):

    def get(self, request):
        prac = Sale.objects.all()
        serializer = SaleSerializer(prac, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleDetail(APIView):

    def get(self,request, pk):
        queryset = Sale.objects.all()
        serializer_class = SaleSerializer



class WydarzeniaLista(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        prac = Wydarzenia.objects.all()
        serializer = WydarzeniaSerializer(prac, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WydarzeniaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=self.request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WlascicielLista(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = WlascicielSerializer


class WlascicielDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = WlascicielSerializer

