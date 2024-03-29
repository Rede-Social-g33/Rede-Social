from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Like


class IsLikeOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Like) -> bool:
        return obj.user == request.user
