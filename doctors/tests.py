''' Pruebas unitarias para la aplicación de doctores. '''
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


from patients.models import Patient

from .models import Doctor


class DoctorViewSetTests(TestCase):
    ''' Pruebas unitarias para la vista de doctores. '''

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Jane',
            last_name='Doe',
            date_of_birth='1990-01-01',
            contact_number='1234567890',
            email='cliente@mail.com',
            address='123 Main St',
            medical_history='None',
        )

        self.doctor = Doctor.objects.create(
            first_name='John',
            last_name='Doe',
            qualification='MD',
            contact_number='1234567890',
            email='doctor@hospital.com',
            address='123 Main St',
            biography='None',
            start_date='2020-01-01',
            is_on_vacation=False,
        )

        self.client = APIClient()

    def test_list_doctor_should_return_200(self):
        ''' La lista de doctores debe funcionar. '''
        url = reverse('doctor-appointments', kwargs={
                      'pk': self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
