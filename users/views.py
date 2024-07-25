from .models import Author,Subscribed
from .serializers import AuthorSerializer,SubscribedSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]


class SubscribedCreateApiView(CreateAPIView):
    queryset = Subscribed.objects.all()
    serializer_class = SubscribedSerializer
    permission_classes = [AllowAny]

class AuthorlistApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class SubscribedListApiView(ListAPIView):
    queryset = Subscribed.objects.all()
    serializer_class = SubscribedSerializer
    permission_classes = [AllowAny]
