'''This file contains the serializers for the Patient, Insurance, and MedicalRecord models. 
The serializers are used to convert the data in the models to JSON format 
so that it can be sent to the frontend.'''
from rest_framework import serializers

from patients.models import Patient, Insurance, MedicalRecord


class PatientSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the Patient model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = Patient
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the Insurance model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = Insurance
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the MedicalRecord model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = MedicalRecord
        fields = '__all__'
