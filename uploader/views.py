from django.shortcuts import render, redirect
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

from .forms import UploadForm, SizeForm, SizeForm2
from .models import MyFileModel, ResizedModel


class BaseView(View):
    """index.html"""

    def get(self, request):
        images = MyFileModel.objects.all()
        template = 'uploader/home.html'
        context = {}

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

        return render(request, 'uploader/add_image.html', context={'form': bound_form})


class ImageDetailView(View):
    """детальное отображение картинки"""

    def get(self, request, pk):
        object_ = MyFileModel.objects.get(pk=pk)
        template = 'uploader/image_detail.html'
        form = SizeForm2()
        context = {'object': object_, 'form': form}

        return render(request, template, context)

    def post(self, request, pk):
        """загрузка изображения"""

        object_ = MyFileModel.objects.get(pk=pk)
        # создаем новую или берем имеющуюся модель с измененными разменрами
        new_object, _ = ResizedModel.objects.get_or_create(original_image=object_)
        bound_form = SizeForm2(request.POST, instance=new_object)

        if bound_form.is_valid():
            resized_image = bound_form.save()
            return render(request, 'uploader/image_resized.html', context={'object': resized_image,
                                                                           'form': bound_form})

        return render(request, 'uploader/image_detail.html', context={'object': object_,
                                                                      'form': bound_form})
