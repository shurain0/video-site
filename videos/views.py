from django.views.generic import ListView
from .models import Video


class VideoListView(ListView):
    model = Video


video_list = VideoListView.as_view()
