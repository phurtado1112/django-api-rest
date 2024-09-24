''' This module registers the models with the admin interface '''
from django.contrib import admin

from .models import Patient, Insurance, MedicalRecord


class PatientAdmin(admin.ModelAdmin):
    ''' This class customizes the admin interface for the Patient model '''
    model = Patient
    list_display = ('first_name', 'last_name', 'contact_number',
                    'email', 'address', 'date_of_birth')


admin.site.register(Patient, PatientAdmin)


class InsuranceAdmin(admin.ModelAdmin):
    ''' This class customizes the admin interface for the Insurance model '''
    model = Insurance
    list_display = ('patient', 'provider', 'policy_number', 'expiration_date')
    search_fields = ('patient', 'provider', 'policy_number', 'expiration_date')
    list_filter = ('expiration_date',)


admin.site.register(Insurance, InsuranceAdmin)


class MedicalRecordAdmin(admin.ModelAdmin):
    ''' This class customizes the admin interface for the MedicalRecord model '''
    model = MedicalRecord
    list_display = ('patient', 'date', 'diagnosis',
                    'treatment', 'follow_up_date')
    search_fields = ('patient', 'date', 'diagnosis',
                     'treatment', 'follow_up_date')
    list_filter = ('date', 'follow_up_date')


admin.site.register(MedicalRecord, MedicalRecordAdmin)
