from django import forms
from django.core.exceptions import ValidationError

from .models import MyFileModel


class UploadForm(forms.ModelForm):
    """форма добавления изображения"""

    url = forms.CharField(max_length=1000,
                          required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control'}),
                          label='Ссылка')

    image = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control'}),
                             label='Файл')

    class Meta:
        model = MyFileModel
        fields = ('url', 'image')

        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class SizeForm(forms.Form):
    """изменение размера изображения"""

    width = forms.CharField(max_length=1000,
                          required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control'}),
                          label='Ширина')
    height = forms.CharField(max_length=1000,
                          required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control'}),
                          label='Высота')

    def clean_width(self):
        new_width = self.cleaned_data['width']
        return  new_width

    def clean_height(self):
        new_height = self.cleaned_data['height']
        return new_height

    def save(self):
        return {'width': self.cleaned_data['width'],
                'height': self.cleaned_data['height']}


