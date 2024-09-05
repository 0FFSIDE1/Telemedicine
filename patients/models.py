from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=20, default=None, null=False, blank=False)
    last_name = models.CharField(max_length=20, default=None, null=False, blank=False)
    date_of_birth = models.DateField(default=None, null=False, blank=False)
    gender = models.CharField(max_length=20, default=None, null=False, blank=False)
    language = models.CharField(default=None, max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.first_name} | {self.last_name}"