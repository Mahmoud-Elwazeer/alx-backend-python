from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow users to access their own data.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only access for safe methods
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object
        return obj.user_id == request.user.id
