# Generated by Django 3.0.6 on 2020-05-14 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0007_auto_20200511_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlesmodel',
            name='likes',
        ),
    ]