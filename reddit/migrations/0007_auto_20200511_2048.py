# Generated by Django 3.0.6 on 2020-05-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0006_commentsmodel_article_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='article_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
