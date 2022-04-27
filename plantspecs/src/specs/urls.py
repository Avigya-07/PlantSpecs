from django.urls import URLPattern, path
from . import views
from django.urls import include


urlpatterns = [
    path('',views.index,name='index'),
    #path('',views.plant_img_upload,name='image-upload'),
    # path('uploaded_images', views.display_plant_images, name='uploaded-images'),
    path('plant/',views.information,name='information'),
    path('PredictImage',views.PredictImage,name='PredictImage')
]
