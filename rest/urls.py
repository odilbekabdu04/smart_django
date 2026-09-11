from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, TovarViewSet, index

router = DefaultRouter()
router.register("rest", CarViewSet, basename="car")
router.register("tovar", TovarViewSet, basename="tovar")

urlpatterns = [
    path('index/', index, name='index'),
]
urlpatterns += router.urls