from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD and OPTIONS requests
        if request.method in SAFE_METHODS:
            return True
        
        # To make POST type requests, the user must be an administrator or a member of the staff
        return request.user and (request.user.is_staff or request.user.is_superuser)
    