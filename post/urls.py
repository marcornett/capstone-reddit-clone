from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('createpost/<str:postType>/', views.createPost, name='create_post'),
    path('postdetail/<int:post_id>/', views.postDetail, name='post_detail'),
    path('addcomment/<int:post_id>/', views.addComment, name='add_comment'),
    path('delete_post/<int:post_id>/<str:sort_by>/', views.delete_post_view, name='delete_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike_post/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('dislike_comment/<int:comment_id>/<int:post_id>/', views.dislike_comment, name='dislike_comment'),
    path('like_comment/<int:comment_id>/<int:post_id>/', views.like_comment, name='like_comment'),
]
