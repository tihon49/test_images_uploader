from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class MyFileModel(models.Model):
    """модель загружаемого файла"""

    url = models.CharField('Ссылка', max_length=500, blank=True, null=True)
    image = models.ImageField('Файл', null=True, blank=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk)


class ResizedModel(models.Model):
    """модель с измененными размерами"""

    original_image = models.ForeignKey(MyFileModel, verbose_name='Оригинал', on_delete=models.CASCADE)
    width = models.IntegerField('Ширина', blank=True, null=True)
    height = models.IntegerField('Высота', blank=True, null=True)

    class Meta:
        verbose_name = 'Измененный файл'
        verbose_name_plural = 'Измененные файлы'
        ordering = ['pk']

    def __str__(self):
        return str(self.pk)
