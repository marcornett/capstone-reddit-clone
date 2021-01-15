from django.urls import path
from reddituser import views


urlpatterns = [
    path('<str:username>/', views.user_profile_view, name='user_profile'),
    path('<str:username>/delete/', views.delete_profile_view, name='delete_profile'),
]

