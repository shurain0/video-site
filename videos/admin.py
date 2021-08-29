from django.contrib import admin
from django.utils.html import format_html

from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', 'title', 'url')
    list_display_links = ('id','thumbnail', 'title')
    search_fields = ('title', 'description')
    list_per_page = 20

    def thumbnail(self, object):
        if object.thumbnail_url:
            return format_html('<img src="{}" width="100">', object.thumbnail_url)

    thumbnail.short_description = 'サムネイル'
    thumbnail.empty_value_display = 'No image'


admin.site.register(Video, VideoAdmin)
