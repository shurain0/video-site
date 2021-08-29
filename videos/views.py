from django.views.generic import ListView, DetailView
from .models import Video


class VideoListView(ListView):
    model = Video


video_list = VideoListView.as_view()

class VideoDetailView(DetailView):
    model = Video


video_detail = VideoDetailView.as_view()
