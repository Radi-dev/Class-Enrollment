from rest_framework import permissions


class ListOrRetrieveIfNotAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated and request.user.is_superuser
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'partial_update']:
            return request.user or request.user.is_superuser
        elif view.action == 'destroy':
            return request.user.is_superuser
        else:
            return False


class NoListIfNotStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff
        else:
            return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'list':
            return request.user.is_staff
        if view.action in ['retrieve', 'create']:
            return True
        elif view.action in ['update', 'partial_update', ]:
            return request.user or request.user.is_superuser
        elif view.action == 'destroy':
            return request.user.is_superuser
        else:
            return False
