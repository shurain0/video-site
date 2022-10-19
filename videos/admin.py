from django.contrib import admin
from django.utils.html import format_html

from .models import Video, Course, Comment, Review


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', 'title', 'url', 'course')
    list_select_related = ('course',)
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('title', 'description')
    list_per_page = 20

    def thumbnail(self, object):
        if object.thumbnail_url:
            return format_html('<img src="{}" width="100">', object.thumbnail_url)

    thumbnail.short_description = 'サムネイル'
    thumbnail.empty_value_display = 'No image'


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_per_page = 20


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'video', 'created_at')
    list_select_related = ('video',)
    list_display_links = ('id', 'text')
    search_fields = ('title', 'description')
    list_per_page: 50

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'course', 'created_at')
    list_select_related = ('author', 'course',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'course')    
    list_per_page: 50


admin.site.register(Video, VideoAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)
