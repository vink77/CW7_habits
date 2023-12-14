from rest_framework.permissions import BasePermission, IsAuthenticated

from users.models import UserRoles

class IsOwnerOrSuperuser(BasePermission):
    message = "Необходимо иметь права владельца или суперпользователя."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user or request.user.is_superuser:
            return True
        return False

