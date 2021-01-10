from django.contrib import admin
from django.urls import path

from post import views as postViews

urlpatterns = [
    path('createpost/<str:postType>/', postViews.createPost, name='create_post'),
    path('postdetail/<int:post_id>/', postViews.postDetail, name='post_detail'),
]
