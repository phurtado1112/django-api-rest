''' This file contains the models for the doctors app. '''
from datetime import date

from django.db import models

# Create your models here.


class Doctor(models.Model):
    ''' This model represents a doctor and has fields '''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    biography = models.TextField()
    start_date = models.DateField(default=date.today)
    is_on_vacation = models.BooleanField(default=False)


class Department(models.Model):
    ''' This model represents a department and has fields '''
    name = models.CharField(max_length=100)
    description = models.TextField()


class DoctorAvailability(models.Model):
    ''' This model represents a doctor's availability and has fields '''
    doctor = models.ForeignKey(
        Doctor, related_name='availabilities', on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class MedicalNote(models.Model):
    ''' This model represents a medical note and has fields '''
    doctor = models.ForeignKey(
        Doctor, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()
