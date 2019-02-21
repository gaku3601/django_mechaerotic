import django_filters
from rest_framework import viewsets, filters

from .models import SexyActress, Video
from .serializer import SexyActressSerializer, VideoSerializer


class SexyActressViewSet(viewsets.ModelViewSet):
    queryset = SexyActress.objects.all()
    serializer_class = SexyActressSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
