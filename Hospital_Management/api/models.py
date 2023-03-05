from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DoctorRegister(models.Model):
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return self.username

class PatientRegister(models.Model):
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return self.username

class PatientDetails(models.Model):
    patient = models.ForeignKey(PatientRegister, related_name='patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorRegister, related_name='doctor', on_delete=models.CASCADE)
    appo_time = models.DateTimeField()

    def __str__(self):
        return self.patient,self.doctor