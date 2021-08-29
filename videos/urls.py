from django.urls import path

from . import views

urlpatterns = [
    path('', views.video_list, name='list'),
    path('detail/<int:pk>', views.Video_detail, name='detail'),
]
