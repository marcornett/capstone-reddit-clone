import django_filters
from subreddit.models import Subreddit
from django_filters import CharFilter

class SubredditFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Subreddit
        fields = ['title']

