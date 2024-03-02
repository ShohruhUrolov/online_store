# from rest_framework.permissions import BasePermission, SAFE_METHODS
#
#
# class IsAdminOrWriteOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return bool(request.user.is_staff and request.user)
#         return True
#
#
# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#