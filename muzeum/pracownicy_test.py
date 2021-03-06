import pytest
import muzeum
from django.urls import reverse


def test_add_prac(admin_client):
    data = {
        'nazwisko' : 'Janowicz',
        'imie' : 'Jan',
        'pesel' : '34985768556',
    }

    url = reverse('muzeumapp:pracownicy')

    response = admin_client.post(
        url,
        data,
        content_type = 'application/json',
    )

    assert response.status_code == 200
    assert response.json() == data
    all_pracownicy = muzeum.muzeumApp.models.Pracownicy.objects.all()
    assert all_pracownicy.count() == 1
    saved_pracownik = all_pracownicy.first()
    assert saved_pracownik.nazwisko == 'Janowicz'
    assert saved_pracownik.imie == 'Jan'
    assert saved_pracownik.pesel == '34985768556'