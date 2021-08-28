from django.shortcuts import render
from django.views.generic import ListView
from .models import Video


class VideoListView(ListView):
    model = Video


list = VideoListView.as_view()
