from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Car, Tovar
from .serializers import CarSerializer, TovarSerializer


def index(request):
    cars = Car.objects.all()
    tovars = Tovar.objects.all()
    return render(request, 'index.html', {'cars': cars, 'tovars': tovars})


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]


class TovarViewSet(viewsets.ModelViewSet):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer
    permission_classes = [AllowAny]