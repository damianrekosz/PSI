from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pracownicy', views.PracownicyLista.as_view()),
    path('eksponaty', views.EksponatyLista.as_view()),
    path('sale', views.SaleLista.as_view()),
    path('wydarzenia', views.WydarzeniaLista.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)