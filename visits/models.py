from django.db import models
from patients.models import Patient
from providers.models import Provider
# Create your models here.
class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient')
    provider =  models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider')
    date_of_visit = models.DateField(default=None, blank=False, null=False)
    date_scheduled =  models.DateField(default=None, null=False, blank=False)
    visit_department_id = models.IntegerField(default=None, null=False, blank=False)
    visit_type = models.CharField(max_length=200, null=False, blank=False, default=None)
    blood_pressure_systolic = models.IntegerField(default=None, blank=True, null=True)
    blood_pressure_diastolic = models.DecimalField(default=None, max_digits=10, decimal_places=2, blank=True, null=True)
    pulse = models.DecimalField(default=None, max_digits=10, decimal_places=2, blank=True, null=True)
    visit_status = models.CharField(max_length=20, default=None, blank=False, null=False)
    def __str__(self) -> str:
        return self.patient.first_name | self.visit_type
    