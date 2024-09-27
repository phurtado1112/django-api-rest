'''This file contains the serializers for the Patient, Insurance, and MedicalRecord models. 
The serializers are used to convert the data in the models to JSON format 
so that it can be sent to the frontend.'''
import datetime
from rest_framework import serializers

from patients.models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer


class PatientSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the Patient model to JSON format.'''

    appointments = AppointmentSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'appointments',
        ]

    def get_age(self, obj):
        '''This method calculates the age of the patient.'''
        return int((datetime.date.today() - obj.date_of_birth).days / 365.25)

    def validate_email(self, value):
        '''This method validates the email field.'''
        if "hospital.com" in value:
            return value
        raise serializers.ValidationError(
            'El correos debe incluir "hospital.com"')


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
