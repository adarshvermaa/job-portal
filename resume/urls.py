from django.urls import path,include
from .views import ResumeApiview,ProfileCompletionStarApiview




urlpatterns = [
    path('resume/', ResumeApiview.as_view(),name="ResumeApiview"),
    path('resume/<int:pk>/', ResumeApiview.as_view(),name="ResumeApiview"),
     
    path('latest-job/', ProfileCompletionStarApiview.as_view(),name="ProfileCompletionStarApiview"),
    path('latest-job/<int:pk>/', ProfileCompletionStarApiview.as_view(),name="ProfileCompletionStarApiview"),
]