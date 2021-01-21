from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('create_point', views.create_point, name='create_point')
]