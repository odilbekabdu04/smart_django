from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullname = models.CharField(max_length=200, blank=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class rest(models.Model):
    """Mahsulot modeli"""
    
    CATEGORY_CHOICES = [
        ('asal', 'Mahalliy asal'),
        ('meva', 'Quritilgan meva'),
        ('yongoq', "Yong'oq"),
        ('boshqa', 'Boshqa'),
    ]
    
    # Asosiy maydonlar
    nomi = models.CharField(max_length=200)
    puli = models.CharField(max_length=100)
    yulduzi = models.CharField(max_length=50, default='5.0')
    korishi = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    # Chegirma uchun
    eski_narx = models.CharField(max_length=100, blank=True, null=True)
    
    # Bo'lib to'lash
    oyiga = models.CharField(max_length=50, blank=True, null=True)
    qancha = models.CharField(max_length=50, blank=True, null=True)
    
    # Yetkazish
    yetkazish_kun = models.CharField(max_length=50, blank=True, null=True, default='2')
    
    # Fermer
    fermer_ismi = models.CharField(max_length=200, blank=True, null=True)
    fermer_manzil = models.CharField(max_length=200, blank=True, null=True)
    
    # Kategoriya
    kategoriya = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='asal'
    )
    
    # Holat
    faol = models.BooleanField(default=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-yaratilgan']
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return f"{self.nomi} — {self.puli} so'm"
    
    @property
    def chegirma_foiz(self):
        """Chegirma foizini hisoblash"""
        try:
            eski = float(self.eski_narx) if self.eski_narx else 0
            yangi = float(self.puli) if self.puli else 0
            if eski > yangi and eski > 0:
                return int(((eski - yangi) / eski) * 100)
        except (ValueError, TypeError):
            pass
        return 0