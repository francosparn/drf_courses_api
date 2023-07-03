from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # If the method is inside GET, HEAD or OPTIONS, allow access
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the user has permission to perform the action
        return obj == request.user