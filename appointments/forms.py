from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'appointment_date', 'message']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }