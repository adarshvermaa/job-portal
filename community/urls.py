from django.urls import path,include
from .views import CommunityParticipationApiview,CommunityReviewsApiview


urlpatterns = [
    path('participation/', CommunityParticipationApiview.as_view(),name="CommunityParticipationApiview"),
    path('participation/<int:pk>/', CommunityParticipationApiview.as_view(),name="CommunityParticipationApiview"),
    path('reviews/<int:pk>/', CommunityReviewsApiview.as_view(),name="CommunityReviewsApiview"),
    path('reviews/<int:pk>/', CommunityReviewsApiview.as_view(),name="CommunityReviewsApiview"),

    
     
]