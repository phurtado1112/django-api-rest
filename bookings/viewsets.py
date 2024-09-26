''' This module defines the viewsets for the Appointment and MedicalNote models '''
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from doctorapp.permissions import IsAdminUser, IsDoctor, IsPatient

from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Appointment model '''
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsDoctor, IsAdminUser, IsPatient]


class MedicalNoteViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the MedicalNote model '''
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
    permission_classes = [IsAuthenticated, IsDoctor, IsPatient]
