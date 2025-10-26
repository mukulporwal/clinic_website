from django.contrib import admin
from appointments.models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'appointment_date', 'message')

admin.site.register(Appointment, AppointmentAdmin)