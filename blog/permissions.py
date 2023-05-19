from rest_framework.permissions import BasePermission
from .models import User

'--------------------------------------------------------------------------------------------------'

class IsCourier(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.COURIER
    
class IsSeller(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.SELLER
    
class IsAssembler(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.ASSEMBLER
    
class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.CUSTOMER
    
class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.ADMIN