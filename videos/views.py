from django.shortcuts import  get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Video, Course, Review
from . import forms


class VideoListView(ListView):
    model = Video


video_list = VideoListView.as_view()


class VideoDetailView(FormMixin, DetailView):
    model = Video
    form_class = forms.CommentForm

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.video = self.object
        instance.save()
        return super(VideoDetailView, self).form_valid(form)


video_detail = VideoDetailView.as_view()


class CourseListView(ListView):
    model = Course

    def get_queryset(self):
        # Viewで表示するクエリセットを取得
        queryset = self.model.objects.prefetch_related(
            'videos').exclude(videos__isnull=True)
        return queryset


course_list = CourseListView.as_view()


class CourseDetailView(DetailView):
    model = Course



course_detail = CourseDetailView.as_view()


class ReviewCreateView(LoginRequiredMixin , CreateView):
    model = Review
    form_class = forms.ReviewForm
    template_name = 'videos/review_form.html'


    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.course_pk})
        # return reverse_lazy('course_list')

    def form_valid(self, form, *args, **kwargs):
        self.course_pk= self.kwargs.get('pk')
        self.course = get_object_or_404(Course, pk=self.course_pk)
        self.instance = form.save(commit=False)
        self.instance.author = self.request.user
        self.instance.course = self.course
        self.instance.save()
        return super().form_valid(form)


review_create = ReviewCreateView.as_view()
