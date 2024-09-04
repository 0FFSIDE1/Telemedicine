from django.db import models

# Create your models here.
class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=20, default=None, null=False, blank=False)
    last_name = models.CharField(max_length=20, default=None, null=False, blank=False)
    provider_speciality = models.CharField(default=None, max_length=225, null=False, blank=False)
    email_address = models.EmailField(max_length=50, unique=True, default=None, null=False, blank=False)
    phone_number = models.CharField(default=None, unique=True, max_length=15, null=False, blank=False)
    date_joined = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name | self.last_name