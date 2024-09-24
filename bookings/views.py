''' This module contains the views for the bookings app '''
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote


class AppointmentListView(ListAPIView, CreateAPIView):
    ''' This class-based view returns a list of all patients '''
    allow_methods = ['GET', 'POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class AppointmentDetailView(RetrieveUpdateDestroyAPIView):  # type: ignore
    ''' This class-based view returns the details of a specific patient '''
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class MedicalNoteListView(ListAPIView, CreateAPIView):
    ''' This class-based view returns a list of all patients '''
    allow_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class MedicalNoteDetailView(RetrieveUpdateDestroyAPIView):  # type: ignore
    ''' This class-based view returns the details of a specific patient '''
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
