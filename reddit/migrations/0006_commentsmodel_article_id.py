# Generated by Django 3.0.6 on 2020-05-11 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0005_auto_20200511_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsmodel',
            name='article_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reddit.ArticlesModel'),
        ),
    ]
