# Generated by Django 3.2.6 on 2021-08-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('url', models.URLField(verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='概要')),
            ],
        ),
    ]