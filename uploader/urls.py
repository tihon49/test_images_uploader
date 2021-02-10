from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.BaseView.as_view(), name='home'),
    path('add_image/', views.AddImageView.as_view(), name='add_image'),
    path('image_detail/<int:pk>/', views.ImageDetailView.as_view(), name='image_detail'),
    # path('image_resized/', views.ImageResizeView.as_view(), name='image_resize'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
