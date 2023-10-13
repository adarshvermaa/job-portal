from django.urls import path,include
from .views import PostJobApiview


urlpatterns = [
     path('latest-job/', PostJobApiview.as_view(),name="PostJobApiview"),
     path('latest-job/<int:pk>/', PostJobApiview.as_view(),name="PostJobApiview"),
     
]
