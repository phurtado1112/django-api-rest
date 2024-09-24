''' This module defines the viewsets for the Patient, MedicalRecord, and Insurance models '''
from rest_framework import viewsets

from .models import Patient, MedicalRecord, Insurance
from .serializers import PatientSerializer, MedicalRecordSerializer, InsuranceSerializer


class PatientViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Patient model '''
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class MedicalRecordViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the MedicalRecord model '''
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Insurance model '''
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
