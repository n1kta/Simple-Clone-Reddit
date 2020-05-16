from django.contrib import admin

from .models import ArticlesModel, LinkModel, CommentsModel

admin.site.register(ArticlesModel)
admin.site.register(LinkModel)
admin.site.register(CommentsModel)