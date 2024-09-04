from django.db import models
from patients.models import Patient
# Create your models here.
class Admission(models.Model):
    admission_id = models.AutoField(primary_key=True, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_admission')
    admission_date = models.DateField(null=False, blank=False, default=None)
    discharge_date = models.DateField(null=False, blank=False, default=None)
    discharge_disposition =  models.CharField(max_length=255, default=None, null=False, blank=False)
    service = models.CharField(max_length=255, null=False, blank=False, default=None)
    primary_diagnosis = models.CharField(max_length=255, default=None, blank=True)

    def __str__(self) -> str:
        return f"Patient: {self.patient.first_name}"