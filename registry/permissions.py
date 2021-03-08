from rest_framework.permissions import BasePermission


class BaseUserPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'getUserLogin':
            return True
        return super().has_permission(request, view)
