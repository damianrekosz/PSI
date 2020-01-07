from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name ='index'),
    path('pracownicy', views.PracownicyLista.as_view()),
    path('pracownicy/<int:pk>', views.PracownicyDetail.as_view()),
    path('eksponaty', views.EksponatyLista.as_view()),
    path('eksponaty/<int:pk>', views.EksponatyDetail.as_view()),
    path('sale', views.SaleLista.as_view()),
    path('sale/<int:pk>', views.SaleDetail.as_view()),
    path('wydarzenia', views.WydarzeniaLista.as_view()),
    path('wydarzenia/<int:pk>', views.WydarzeniaDetail.as_view()),
    path('wlascicielowiowie', views.WlascicielLista.as_view()),
    path('wlascicielowiowie/<int:pk>', views.WlascicielDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)