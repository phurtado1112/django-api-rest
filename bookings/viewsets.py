from rest_framework import viewsets

from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Appointment model '''
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class MedicalNoteViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the MedicalNote model '''
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
