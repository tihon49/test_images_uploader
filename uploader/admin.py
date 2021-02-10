from django.contrib import admin
from .models import MyFileModel


@admin.register(MyFileModel)
class FileAdmin(admin.ModelAdmin):
    pass


