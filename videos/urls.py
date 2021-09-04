from django.urls import path

from . import views

urlpatterns = [
    path('', views.video_list, name='list'),
    path('<int:pk>/', views.video_detail, name='detail'),
    path('course/', views.course_list, name='course_list'),
]
