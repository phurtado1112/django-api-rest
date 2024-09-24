'''This file contains the viewsets for the Doctor model.'''
from rest_framework import viewsets

from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Doctor model '''
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Department model '''
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the DoctorAvailability model '''
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer


class MedicalNoteViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the MedicalNote model '''
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
