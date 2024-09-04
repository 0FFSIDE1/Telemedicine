from django.db import models
from patients.models import Patient
from admissions.models import Admission
# Create your models here.
class Discharge(models.Model):
    discharge_id = models.AutoField(primary_key=True, editable=False)
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE, related_name='discharge')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_discharge')
    discharge_date = models.DateField(null=False, blank=False, default=None)
    discharge_disposition =  models.CharField(max_length=255, default=None, null=False, blank=False)
   
    def __str__(self) -> str:
        return f"Patient: {self.patient.first_name}"