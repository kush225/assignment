
from rest_framework import permissions
from api.models.user import User
from api.models.user import TYPE_CHOICES


class IsBrandUser(permissions.BasePermission):
	"""
	Allows access only to authenticated brand users.
	"""
	def has_permission(self, request, view):
		return bool(request.user and hasattr(request.user, 'type') and request.user.type  == TYPE_CHOICES[1][0])


class IsCustomer(permissions.BasePermission):
	"""
	Allows access only to authenticated customer users.
	"""
	def has_permission(self, request, view):
		return bool(request.user and hasattr(request.user, 'type') and request.user.type == TYPE_CHOICES[0][0])