from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.RentViewSet, basename="rent")

urlpatterns = [
    path('rent/', include(router.urls)),
]