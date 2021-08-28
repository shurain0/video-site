from django.db import models
import re


class Video(models.Model):

    title = models.CharField(verbose_name='タイトル', max_length=255)
    url = models.URLField(verbose_name='URL')
    description = models.TextField(verbose_name='概要', null=True, blank=True)

    @property
    def video_id(self):
        YT_URL = "https://youtu.be/(.*){11}"
        return re.match(YT_URL, str(self.url)).group()[-11:]

    @property
    def thumbnail_url(self):
        THUMBNAIL_URL = "https://img.youtube.com/vi/{}/mqdefault.jpg"

        if self.video_id:
            return THUMBNAIL_URL.format(self.video_id)
        return ""

    def __str__(self):
        return self.title
