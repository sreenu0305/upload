from django.urls import path
from . import views

urlpatterns = [
    path('', views.load, name='load'),
    path('upload/', views.upload, name='upload'),
    path('all_list/', views.all_objects, name='all_list'),
]
