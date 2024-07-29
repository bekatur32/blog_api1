from rest_framework.permissions import BasePermission

class CanCreateBlogPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.can_create_blogs


class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Подписчик').exists()
