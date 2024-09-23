''' This file contains the models for the bookings app. '''
from django.db import models
from doctors.models import Doctor
from patients.models import Patient


class Appointment(models.Model):
    ''' This model represents an appointment and has fields '''
    patient = models.ForeignKey(
        Patient, related_name='appointments', on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        Doctor, related_name='appointments', on_delete=models.CASCADE
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField()
    status = models.CharField(max_length=10)


class MedicalNote(models.Model):
    ''' This model represents a medical note and has fields '''
    appointment = models.ForeignKey(
        Appointment, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()
