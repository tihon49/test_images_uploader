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

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})

    def clean(self):
        """убеждаемся что только одно из полей заполненно"""

        if self.url and self.image:
            raise ValidationError("Долножно быть указано что-то одно.")

    def __str__(self):
        return self.id
