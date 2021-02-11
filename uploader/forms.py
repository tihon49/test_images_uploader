from django import forms
from django.db.models import Q

from .models import MyFileModel


class UploadForm(forms.ModelForm):
    """форма добавления изображения"""

    class Meta:
        model = MyFileModel
        fields = ('url', 'image')

        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """валидация формы"""

        cleaned_data = super().clean()
        new_url = self.cleaned_data['url']
        new_image = self.cleaned_data['image']

        if new_url and new_image:
            raise forms.ValidationError('Нужно заполнить только одно поле.')
        elif not new_url and not new_image:
            raise forms.ValidationError('Одно из полей должно быть заполненно.')


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
        return new_width

    def clean_height(self):
        new_height = self.cleaned_data['height']
        return new_height

    def save(self):
        return {'width': self.cleaned_data['width'],
                'height': self.cleaned_data['height']}
