# filters.py
import django_filters
from .models import PostJob

class PostJobFilter(django_filters.FilterSet):
    class Meta:
        model = PostJob
        fields = {
            'job_category__category': ['exact'],
            'company_name': ['exact'],
            'job_title': ['icontains'],
            'last_date': ['exact'],
            'skills': ['icontains'],
            'description': ['icontains'],
        }
