''' This file contains the views for the patients app. '''
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PatientSerializer
from .models import Patient


class PatientListView(ListAPIView, CreateAPIView):
    ''' This class-based view returns a list of all patients '''
    allow_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class PatientDetailView(RetrieveUpdateDestroyAPIView):  # type: ignore
    ''' This class-based view returns the details of a specific patient '''
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
