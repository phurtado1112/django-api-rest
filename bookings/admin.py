''' This module registers the models with the admin site '''
from django.contrib import admin

from .models import Appointment, MedicalNote


class AppointmentAdmin(admin.ModelAdmin):
    ''' This class-based view returns the details of a specific patient '''
    model = Appointment
    list_display = ('id', 'patient', 'doctor', 'appointment_date',
                    'appointment_time', 'status')
    list_filter = ('status', 'doctor', 'appointment_date')
    search_fields = ('patient__first_name', 'patient__last_name',
                     'doctor__first_name', 'doctor__last_name', 'reason')
    list_per_page = 25


admin.site.register(Appointment, AppointmentAdmin)


class MedicalNoteAdmin(admin.ModelAdmin):
    ''' This class-based view returns the details of a specific patient '''
    model = MedicalNote
    list_display = ('id', 'appointment', 'note', 'date')
    list_filter = ('date',)
    search_fields = ('note', 'appointment__patient__first_name',
                     'appointment__patient__last_name')
    list_per_page = 25


admin.site.register(MedicalNote, MedicalNoteAdmin)
