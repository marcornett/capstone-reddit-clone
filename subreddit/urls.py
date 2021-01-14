from django.urls import path
from subreddit import views

urlpatterns = [
    path('page/<str:title>/<str:sort_by>/', views.subreddit_view, name='subreddit'),
    path(
        'create_subreddit/',
        views.subreddit_creation_view,
        name='create_subreddit'
        )
]
