from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
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
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer

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


class PracownicyDetail(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Pracownicy.objects.all()
    serializer_class = PracownicySerializer

    def get(self, request, pk):
        prac = Pracownicy.objects.filter(id=pk)
        serializer = PracownicySerializer(prac, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        prac = Pracownicy.objects.filter(id=pk)
        prac.delete()





class EksponatyLista(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Eksponaty.objects.all()
    serializer_class = EksponatySerializer

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


class EksponatyDetail(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Eksponaty.objects.all()
    serializer_class = EksponatySerializer

    def get(self, request, pk):
        prac = Eksponaty.objects.filter(id=pk)
        serializer = EksponatySerializer(prac, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        prac = Eksponaty.objects.filter(id=pk)
        prac.delete()


class SaleLista(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

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


class SaleDetail(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def get(self, request, pk):
        prac = Sale.objects.filter(id = pk)
        serializer = SaleSerializer(prac, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        prac = Sale.objects.filter(id=pk)
        prac.delete()


class WydarzeniaLista(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Wydarzenia.objects.all()
    serializer_class = WydarzeniaSerializer

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


class WydarzeniaDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Wydarzenia.objects.all()
    serializer_class = WydarzeniaSerializer

    def put(self, request, pk):
        prac = Wydarzenia.objects.filter(id=pk)
        serializer = WydarzeniaSerializer(prac, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def get(self, request, pk):
        prac = Wydarzenia.objects.filter(id=pk)
        serializer = WydarzeniaSerializer(prac, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        prac = Wydarzenia.objects.filter(id=pk)
        prac.delete()
        


class WlascicielLista(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = WlascicielSerializer


class WlascicielDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = WlascicielSerializer

