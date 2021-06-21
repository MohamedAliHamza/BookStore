from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "You do not have access to this page"

    def has_object_permission(self, request, view, obj):
        return obj.client == request.user
