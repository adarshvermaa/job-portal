from django.urls import path,include
from .views import PostJobApiview,PostJobViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'filter', PostJobViewSet, basename='filter')
urlpatterns = [
    path('latest-job/', PostJobApiview.as_view(),name="PostJobApiview"),
    path('latest-job/<int:pk>/', PostJobApiview.as_view(),name="PostJobApiview"),
    path('job/', include(router.urls)),
     
]
