from rest_framework import serializers
from .models import Car, Tovar


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tovar
        fields = '__all__'