''' This file contains the models for the patients app. 
The Patient model represents a patient and has fields. 
The Insurance model represents an insurance policy for a patient and has fields. 
The MedicalRecord model represents a medical record for a patient and has fields. '''
from django.db import models

# Create your models here.


class Patient(models.Model):
    ''' This model represents a patient and has fields '''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    medical_history = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Insurance(models.Model):
    ''' This model represents an insurance policy for a patient and has fields '''
    patient = models.ForeignKey(
        Patient, related_name='insurances', on_delete=models.CASCADE
    )
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    expiration_date = models.DateField()

    def __str__(self):
        return f'{self.patient} - {self.provider}'


class MedicalRecord(models.Model):
    ''' This model represents a medical record for a patient and has fields '''
    patient = models.ForeignKey(
        Patient, related_name='medical_records', on_delete=models.CASCADE
    )
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    follow_up_date = models.DateField()

    def __str__(self):
        return f'{self.patient} - {self.date}'
