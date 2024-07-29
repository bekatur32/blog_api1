from .models import Subscribed
from .serializers import SubscribedSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

# Create your views here.
class SubscribedCreateApiView(CreateAPIView):
    queryset = Subscribed.objects.all()
    serializer_class = SubscribedSerializer
    permission_classes = [AllowAny]
class SubscribedListApiView(ListAPIView):
    queryset = Subscribed.objects.all()
    serializer_class = SubscribedSerializer
    permission_classes = [AllowAny]
