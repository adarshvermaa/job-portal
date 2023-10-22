from django.urls import path,include
from .views import ApplyJobApiview


urlpatterns = [
    path('apply/', ApplyJobApiview.as_view(),name="ApplyJobApiview"),
    
     
]