''' This module contains the views for the doctors app '''
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorListView(ListAPIView, CreateAPIView):
    ''' This class-based view returns a list of all patients '''
    allow_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DoctorDetailView(RetrieveUpdateDestroyAPIView):  # type: ignore
    ''' This class-based view returns the details of a specific patient '''
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DepartmentListView(ListAPIView, CreateAPIView):
    ''' This class-based view returns a list of all patients '''
    allow_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentDetailView(RetrieveUpdateDestroyAPIView):  # type: ignore
    ''' This class-based view returns the details of a specific patient '''
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DoctorAvailabilityView(ListAPIView, CreateAPIView):
    ''' This class-based view returns a list of all patients '''
    allow_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DoctorAvailabilityDetailView(RetrieveUpdateDestroyAPIView):  # type: ignore
    ''' This class-based view returns the details of a specific patient '''
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class MedicalNoteView(ListAPIView, CreateAPIView):
    ''' This class-based view returns a list of all patients '''
    allow_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class MedicalNoteDetailView(RetrieveUpdateDestroyAPIView):
    ''' This class-based view returns the details of a specific patient '''
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
