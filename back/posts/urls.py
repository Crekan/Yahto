from django.urls import path
from .views import post_comment, like_unlike_post

app_name = 'posts'

urlpatterns = [
    path('', post_comment, name='post-comment'),
    path('liked/', like_unlike_post, name='like-post'),
]
