from django.urls import path
from .views import SubscribedListApiView, SubscribedCreateApiView

urlpatterns = [
    path('sub/', SubscribedListApiView.as_view(), name='sub-list'),
    path('sub/create/', SubscribedCreateApiView.as_view(), name='sub-create'),

]
