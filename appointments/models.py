from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    appointment_date = models.DateField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.appointment_date}"