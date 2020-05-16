from django.urls import path

from .views import (
    home,
    article_view,
    new_article,
    search,
    links,
    new_link,
    like,
    dislike,
    profile_view,
    profile_post,
    profile_comments,
    comments_like,
    comments_dislike,
    edit_article,
    delete_article,
    edit_comment,
    delete_comment,
)

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('new/', new_article, name='new_article'),
    path('article/<int:article_id>/', article_view, name='article_view'),
    path('article/update/<int:article_id>/', edit_article, name='edit_article'),
    path('article/delete/<int:article_id>/', delete_article, name='delete_article'),

    path('subbeddit/<str:link_name>/', links, name='links'),
    path('new/link/', new_link, name='new_link'),

    path('article/<int:article_id>/like', like, name='like'),
    path('article/<int:article_id>/dislike', dislike, name='dislike'),
    path('article/<int:article_id>/comments/<int:comment_id>/like', comments_like, name='comments_like'),
    path('article/<int:article_id>/comments/<int:comment_id>/dislike', comments_dislike, name='comments_dislike'),
    path('article/<int:article_id>/comments/update/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('article/<int:article_id>/comments/delete/<int:comment_id>/', delete_comment, name='delete_comment'),

    path('<str:profile_name>/', profile_view, name='profile_view'),
    path('<str:profile_name>/post', profile_post, name='profile_post'),
    path('<str:profile_name>/comments', profile_comments, name='profile_comments'),
]