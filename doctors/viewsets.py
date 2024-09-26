'''This file contains the viewsets for the Doctor model.'''
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from doctorapp.permissions import IsDoctor, IsAdminUser

from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer
)


class DoctorViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Doctor model '''
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

    @action(detail=True, methods=['post'], url_path='set-on-vacation')
    def set_on_vacation(self, request, pk=None):
        ''' This method sets the is_on_vacation field of a doctor to True '''
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({'status': 'Doctor está en vacaciones'})

    def set_off_vacation(self, request, pk=None, url_path='set-off-vacation'):
        ''' This method sets the is_on_vacation field of a doctor to False '''
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({'status': 'El doctor regresó de vacaciones'})


class DepartmentViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Department model '''
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the DoctorAvailability model '''
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer


class MedicalNoteViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the MedicalNote model '''
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
    permission_classes = [IsAuthenticated, IsDoctor]
