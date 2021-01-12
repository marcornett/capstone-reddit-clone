from django.urls import path
from subreddit import views

urlpatterns = [
    path('<str:title>', views.subreddit_view, name='subreddit'),
]
