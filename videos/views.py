from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Video


class VideoListView(ListView):
    model = Video


video_list = VideoListView.as_view()

class VideoDetailView(LoginRequiredMixin, DetailView):
    model = Video


video_detail = VideoDetailView.as_view()
