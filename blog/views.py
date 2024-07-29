from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Blog, Author
from .serializers import BlogSerializer, BlogputSerializer
from .permishions import CanCreateBlogPermission,IsSubscriber



class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        article = self.get_object()
        if article.is_premium:
            return [IsAuthenticatedOrReadOnly(), IsSubscriber()]
        return [IsAuthenticatedOrReadOnly()]

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        if article.is_premium and not request.user.groups.filter(name='Подписчик').exists():
            return Response({"detail": "You do not have permission to access this article."}, status=403)
        return super().get(request, *args, **kwargs)


class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [CanCreateBlogPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogputSerializer
    permission_classes = [CanCreateBlogPermission]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [CanCreateBlogPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)