from django.urls import path,include
from .views import PostSectionApiview,PostCategoryApiview


urlpatterns = [
    path('post/', PostSectionApiview.as_view(),name="PostSectionApiview"),
    path('category/', PostCategoryApiview.as_view(),name="PostCategoryApiview"),
    path('post/<int:pk>/', PostSectionApiview.as_view(),name="PostSectionApiview"),
    path('category/<int:pk>/', PostCategoryApiview.as_view(),name="PostCategoryApiview"),

    
     
]