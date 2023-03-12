from rest_framework import permissions
from rest_framework.views import Request, View
from connections.models import Connection
from .models import Post
from django.db.models import Q


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS or request.user.is_authenticated
        )


class IsPostOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Post) -> bool:
        print(obj.user, request.user)
        return obj.user == request.user
