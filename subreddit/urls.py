from django.urls import path
from subreddit import views

urlpatterns = [
    path(
        'page/<str:title>/<str:sort_by>/',
        views.subreddit_view,
        name='subreddit'
        ),
    path(
        'create_subreddit/',
        views.subreddit_creation_view,
        name='create_subreddit'
        ),
    path('search/', views.subreddit_search_view, name='subreddit_search'),
    path('subscribe/<int:subreddit_id>/', views.subscribe, name='subscribe_subreddit'),
    path('unsubscribe/<int:subreddit_id>/', views.unsubscribe, name='unsubscribe_subreddit'),
]
