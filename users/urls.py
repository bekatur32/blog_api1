from django.urls import path
from .views import AuthorCreateApiView, SubscribedCreateApiView, AuthorlistApiView, SubscribedListApiView

urlpatterns = [
    path('authors/', AuthorlistApiView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateApiView.as_view(), name='author-create'),
    path('subscribed/', SubscribedListApiView.as_view(), name='subscribed-list'),
    path('subscribed/create/', SubscribedCreateApiView.as_view(), name='subscribed-create'),
]
