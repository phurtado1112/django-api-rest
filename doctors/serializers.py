'''This module contains the serializer classes for the Doctor, Department, 
DoctorAvailability, and MedicalNote models.'''
from datetime import date
from rest_framework import serializers

from doctors.models import Department, Doctor, DoctorAvailability, MedicalNote
from bookings.serializers import AppointmentSerializer


class DoctorSerializer(serializers.ModelSerializer):
    '''This serializer class is used to convert the Doctor model to JSON format.'''

    appointments = AppointmentSerializer(many=True, read_only=True)
    experience_years = serializers.SerializerMethodField()

    class Meta:
        '''This inner Meta class defines the model and fields to be serialized.'''
        model = Doctor
        fields = [
            'id',
            'first_name',
            'last_name',
            'qualification',
            'contact_number',
            'email',
            'address',
            'biography',
            'start_date',
            'is_on_vacation',
            'appointments',
            'experience_years',
        ]

    def get_experience_years(self, obj):
        '''This method calculates the experience of the doctor in years.'''
        return int((date.today() - obj.start_date).days / 365.25)

    def validate_email(self, value):
        '''This method validates the email field.'''
        if "hospital.com" in value:
            return value
        raise serializers.ValidationError(
            'El correos debe incluir "hospital.com"')


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
