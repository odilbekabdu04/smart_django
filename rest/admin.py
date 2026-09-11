from django.contrib import admin
from .models import Car, Tovar

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'puli', 'yulduzi', 'korishi')


@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_created')