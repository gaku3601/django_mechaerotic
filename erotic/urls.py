from rest_framework import routers
from .views import SexyActressViewSet, VideoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'sexy-actress', SexyActressViewSet)
router.register(r'video', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
