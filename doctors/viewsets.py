'''This file contains the viewsets for the Doctor model.'''
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment
from doctorapp.permissions import IsAdminUser, IsDoctor

from .models import Department, Doctor, DoctorAvailability, MedicalNote
from .serializers import (DepartmentSerializer, DoctorAvailabilitySerializer,
                          DoctorSerializer, MedicalNoteSerializer)


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

    @action(detail=True, methods=['post'], url_path='set-off-vacation')
    def set_off_vacation(self, request, pk=None):
        ''' This method sets the is_on_vacation field of a doctor to False '''
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({'status': 'El doctor regresó de vacaciones'})

    @action(detail=True, methods=['get', 'post'],
            serializer_class=AppointmentSerializer, url_path='appointments')
    def appointments(self, request, pk=None):
        ''' This method returns the appointments of a doctor '''
        doctor = self.get_object()

        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'], url_path='delete-appointment/(?P<appointment_id>[^/.]+)')
    def delete_appointment(self, request, pk=None, appointment_id=None):
        doctor = self.get_object()  # Obtener el doctor por su ID
        try:
            # Intentamos obtener la cita para ese doctor y con el ID proporcionado
            appointment = Appointment.objects.get(
                id=appointment_id, doctor=doctor)
            appointment.delete()  # Eliminar la cita
            return Response({"status": "Cita eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response({"error": "Cita no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    # @action(detail=True, methods=['delete', 'get'], url_path='appointments/(?P<appointment_id>[^/.]+)')
    # def appointment_delete(self, request, appointment_id=None):
    #     ''' This method deletes an appointment of a doctor '''
    #     doctor = self.get_object()
    #     appointment = Appointment.objects.get(appointment_id, doctor=doctor)
    #     appointment.delete()
    #     return Response({'status': 'Cita eliminada'}, status=status.HTTP_200_OK)


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
