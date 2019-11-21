from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from projektMuzeum.Projekt.muzeumApp import seralizers as ser



@csrf_exempt
def question_list(request):
    global serializer
    if request.method == 'GET':
        pracownicy= ser.pracownik.objects.all()
        serializer = ser.PracownikSeralizer(pracownicy, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ser.PracownikSeralizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def question_detail(request, pk):
    try:
        pracownik = ser.pracownik.objects.get(pk=pk)
    except ser.pracownik.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ser.PracownikSeralizer(pracownik)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ser.PracownikSeralizer(pracownik, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        ser.pracownik.delete()
        return HttpResponse(status=204)
