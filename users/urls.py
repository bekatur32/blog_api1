from django.urls import path
from .views import AuthorCreateApiView, AuthorlistApiView

urlpatterns = [
    path('authors/', AuthorlistApiView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateApiView.as_view(), name='author-create'),

]
