from django.contrib import admin
from .models import MyFileModel, ResizedModel


@admin.register(MyFileModel)
class FileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'url', 'image']


@admin.register(ResizedModel)
class FileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'original_image', 'width', 'height']

