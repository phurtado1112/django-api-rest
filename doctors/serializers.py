'''This module contains the serializer classes for the Doctor, Department, 
DoctorAvailability, and MedicalNote models.'''
from rest_framework import serializers

from doctors.models import Department, Doctor, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the Doctor model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = Doctor
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the Department model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = Department
        fields = '__all__'


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the DoctorAvailability model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = DoctorAvailability
        fields = '__all__'


class MedicalNoteSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the MedicalNote model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = MedicalNote
        fields = '__all__'
