from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Video, Course


class VideoListView(ListView):
    model = Video


video_list = VideoListView.as_view()

class VideoDetailView(LoginRequiredMixin, DetailView):
    model = Video


video_detail = VideoDetailView.as_view()


class CourseListView(ListView):
    model = Course

    def get_queryset(self):
        # Viewで表示するクエリセットを取得
        queryset = self.model.objects.prefetch_related('videos').exclude(videos__isnull=True)
        return queryset


course_list = CourseListView.as_view()
