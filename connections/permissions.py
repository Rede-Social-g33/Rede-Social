from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Connection


class IsConnectionsOwner(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, connection: Connection
    ) -> bool:
        return connection.user == request.user
