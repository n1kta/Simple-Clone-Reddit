# Generated by Django 3.0.6 on 2020-05-10 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0002_linkmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesmodel',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reddit.LinkModel'),
        ),
    ]
