from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Avg

from .models import Video, Course, Review
from . import forms


class VideoListView(ListView):
    model = Video


video_list = VideoListView.as_view()


class VideoDetailView(LoginRequiredMixin, FormMixin, DetailView):
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

    # def get_context_data(self, **kwargs):
    #     context = super(CourseDetailView, self).get_context_data(**kwargs)
    #     instance = self.model.objects.filter(
    #         id=self.kwargs.get('id')).prefetch_related('reviews')
    #     reviews_avg = instance.aggregate(avg=Avg('reviews__rating'))['avg']
    #     reviews_count = instance.count()
    #     context['reviews_avg'] = reviews_avg
    #     context['reviews_count'] = reviews_count
    #     return context


course_detail = CourseDetailView.as_view()


class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'text', 'rating']

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.pk})
        # return reverse_lazy('course_list')

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
        instance.course = self.object.course
        instance.save()
        return super().form_valid(form)


review_create = ReviewCreateView.as_view()
