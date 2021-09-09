# Generated by Django 3.1.1 on 2021-09-09 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_auto_20210904_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='videos.video', verbose_name='動画')),
            ],
        ),
    ]
