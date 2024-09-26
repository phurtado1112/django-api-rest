''' Este módulo define los permisos para los doctores '''
from rest_framework import permissions


class IsDoctor(permissions.BasePermission):  # type: ignore
    ''' Esta clase define el permiso para el Doctor '''

    def has_permission(self, request, view):
        ''' Este método verifica si el usuario es un doctor '''
        return request.user.groups.filter(name='doctors').exists()


class IsAdminUser(permissions.BasePermission):  # type: ignore
    ''' Esta clase define el permiso para el administrador '''

    def has_permission(self, request, view):
        ''' Este método verifica si el usuario es un administrador '''
        return request.user.groups.filter(name='admin').exists()


class IsPatient(permissions.BasePermission):  # type: ignore
    ''' Esta clase define el permiso para el paciente '''

    def has_permission(self, request, view):
        ''' Este método verifica si el usuario es un paciente '''
        return request.user.groups.filter(name='patients').exists()
