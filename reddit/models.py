from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class LinkModel(models.Model):
    subbeddit = models.CharField(max_length=255)

    def __str__(self):
        return self.subbeddit


class ArticlesModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(LinkModel, null=True, blank=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        return self.title


class CommentsModel(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    article_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='comments_likes', blank=True)

    def get_date(self):
        time = datetime.now()
        if self.created.day == time.day:
            return str(time.hour - self.created.hour) + " hours ago"
        else:
            if self.created.month == time.month:
                return f"{time.day - self.created.day} days ago"
            else:
                if self.created.year == time.year:
                    return f"{time.month - self.created.month} months ago"
        return self.created

    def __str__(self):
        return self.text


