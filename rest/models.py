from django.db import models


class Car(models.Model):
    nomi = models.CharField(max_length=100)
    puli = models.IntegerField()
    yulduzi = models.CharField(max_length=100)
    korishi = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)

    def __str__(self):
        return f"{self.nomi} {self.model} ({self.yulduzi})"


class Tovar(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_created = models.BooleanField(default=False)

    def __str__(self):
        return self.name