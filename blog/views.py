from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Blog, Author
from .serializers import BlogSerializer, BlogputSerializer
from .permishions import CanCreateBlogPermission


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [CanCreateBlogPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)