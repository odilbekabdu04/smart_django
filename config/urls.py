from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Admin panel sarlavhalari
admin.site.site_header = "Zenzo Market Admin"
admin.site.site_title = "Zenzo Market"
admin.site.index_title = "Boshqaruv paneli"

urlpatterns = [
    # ✅ ADMIN PANEL — /rest/ da
    path('rest/', admin.site.urls),
    
    # API manzillar
    path('api/', include('rest.urls')),
]

# Media fayllar (rasmlar uchun)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)