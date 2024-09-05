from django.db import models
from patients.models import Patient
from visits.models import Visit
# Create your models here.
class Ed_visit(models.Model):
    ed_visit_id = models.AutoField(primary_key=True, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name='visit')
    acuity = models.IntegerField(default=None, null=False, blank=False)
    reason_for_visit = models.CharField(max_length=255, default=None, null=False, blank=False)
    disposition = models.CharField(max_length=255, null=False, blank=False, default=None)
    def __str__(self) -> str:
        return f"{self.patient.first_name} | {self.visit}"
    