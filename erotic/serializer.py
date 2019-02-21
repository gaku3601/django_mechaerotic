from rest_framework import serializers

from .models import SexyActress, Video


class SexyActressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SexyActress
        fields = ('name', 'memo')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'sexyActress', 'url', 'memo')
