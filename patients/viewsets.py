''' This module defines the viewsets for the Patient, MedicalRecord, and Insurance models '''
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from doctorapp.permissions import IsAdminUser, IsDoctor

from .models import Insurance, MedicalRecord, Patient
from .serializers import (InsuranceSerializer, MedicalRecordSerializer,
                          PatientSerializer)


class PatientViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Patient model '''
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsDoctor, IsAdminUser]


class MedicalRecordViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the MedicalRecord model '''
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated, IsDoctor]


class InsuranceViewSet(viewsets.ModelViewSet):
    ''' This class defines the viewset for the Insurance model '''
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
