'''This module contains the serializer classes for the bookings app.'''
from rest_framework import serializers

from bookings.models import Appointment, MedicalNote


class AppointmentSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the Appointment model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = Appointment
        fields = '__all__'


class MedicalNoteSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the MedicalNote model to JSON format.'''
    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = MedicalNote
        fields = '__all__'
