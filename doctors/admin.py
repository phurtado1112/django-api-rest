''' This module registers the models with the admin interface '''
from django.contrib import admin
from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorAdmin(admin.ModelAdmin):
    ''' This class customizes the admin interface for the Doctor model '''
    model = Doctor
    list_display = ('first_name', 'last_name', 'qualification',
                    'contact_number', 'email', 'address', 'biography')
    search_fields = ('first_name', 'last_name', 'qualification',
                     'contact_number', 'email', 'address', 'biography')
    list_filter = ('qualification',)


admin.site.register(Doctor, DoctorAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    ''' This class customizes the admin interface for the Department model '''
    model = Department
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Department, DepartmentAdmin)


class DoctorAvailabilityAdmin(admin.ModelAdmin):
    ''' This class customizes the admin interface for the DoctorAvailability model '''
    mpdel = DoctorAvailability
    list_display = ('doctor', 'start_date', 'end_date',
                    'start_time', 'end_time')
    search_fields = ('doctor', 'start_date', 'end_date',
                     'start_time', 'end_time')
    list_filter = ('start_date', 'end_date', 'start_time', 'end_time')


admin.site.register(DoctorAvailability, DoctorAvailabilityAdmin)


class MedicalNoteAdmin(admin.ModelAdmin):
    ''' This class customizes the admin interface for the MedicalNote model '''
    model = MedicalNote
    list_display = ('doctor', 'note', 'date')
    search_fields = ('doctor', 'note', 'date')
    list_filter = ('date',)


admin.site.register(MedicalNote, MedicalNoteAdmin)
