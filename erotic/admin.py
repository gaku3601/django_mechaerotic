from django.contrib import admin
from .models import SexyActress, Video

@admin.register(SexyActress)
class SexyActress(admin.ModelAdmin):
    pass

@admin.register(Video)
class Video(admin.ModelAdmin):
    pass
