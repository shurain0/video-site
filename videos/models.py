from django.db import models
import re


class Video(models.Model):
    class Meta:
        db_table = 'video'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    url = models.URLField(verbose_name='URL')
    description = models.TextField(verbose_name='概要', null=True, blank=True)

    @property
    def video_id(self):
        yt_url = "https://youtu.be/(.*)"
        return re.findall(yt_url, str(self.url))[0]

    @property
    def thumbnail_url(self):
        img_url = "https://img.youtube.com/vi/"

        if self.video_id:
            return f"{img_url}{self.video_id}/mqdefault.jpg"
        return ""

    def __str__(self):
        return self.title
