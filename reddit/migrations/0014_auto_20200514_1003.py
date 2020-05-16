# Generated by Django 3.0.6 on 2020-05-14 10:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit', '0013_articlesmodel_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesmodel',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
