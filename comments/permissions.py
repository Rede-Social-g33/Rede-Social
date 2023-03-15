from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Comment


class IsCommentOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Comment) -> bool:
        return obj.user == request.user
