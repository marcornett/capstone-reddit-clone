from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('createpost/<str:postType>/', views.createPost, name='create_post'),
    path('postdetail/<int:post_id>/', views.postDetail, name='post_detail'),
    path('addcomment/<int:post_id>/', views.addComment, name='add_comment'),
    path('delete_post/<int:post_id>/', views.delete_post_view, name='delete_post'),
    path('like_dis_post/<int:post_id>/<str:like_dis>/', views.like_dis_post, name='like_dis_post'),
    path('like_dis_comment/<int:comment_id>/<int:post_id>/<str:like_dis>/', views.like_dis_comment, name='like_dis_comment'),
]
