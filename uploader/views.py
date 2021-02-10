from django.shortcuts import render, redirect
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

from .forms import UploadForm, SizeForm
from .models import MyFileModel


class BaseView(View):
    """index.html"""

    def get(self, request):
        images = MyFileModel.objects.all()
        template = 'uploader/home.html'
        context = {'data': 'Какие-то данные'}

        if images:
            context['objects_list'] = images

        return render(request, template, context)


class AddImageView(View):
    """добавление изображения"""

    def get(self, request):
        template = 'uploader/add_image.html'
        form = UploadForm
        context = {'form': form}

        return render(request, template, context)

    def post(self, request):
        template = 'uploader/home.html'
        bound_form = UploadForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_image = bound_form.save()
            return redirect(new_image)

        return render(request, template, context={'form': bound_form})


class ImageDetailView(View):
    """детальное отображение картинки"""

    def get(self, request, pk):
        object_ = MyFileModel.objects.get(pk=pk)
        template = 'uploader/image_detail.html'
        form = SizeForm()
        context = {'object': object_, 'form': form}

        return render(request, template, context)

    def post(self, request, pk):
        # TODO: реализовать изменение размеров изображения
        object_ = MyFileModel.objects.get(pk=pk)
        bound_form = SizeForm(request.POST)

        if bound_form.is_valid():
            print('Form is valid!')
            data = bound_form.save()

            return render(request, 'uploader/image_resized.html', context={'data': data,
                                                                           'object': object_,
                                                                           'form': bound_form})

        return render(request, 'uploader/image_detail.html', {'object': object_})


# class ImageResizeView(View):
#     def get(self, request):
#         template = 'uploader/image_resized.html'
#         form = SizeForm()
#
#         return render()