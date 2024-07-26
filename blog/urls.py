from django.urls import path
from .views import  BlogCreateView, BlogUpdateView, BlogDeleteView,BlogListView

urlpatterns = [
    path('blogs/list/',BlogListView.as_view(), name='blog_list'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]