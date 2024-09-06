from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from patients.models import Patient
from visits.models import Visit
from django.contrib import messages
from rest_framework import status

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    

def create_patient_record(request, data):
    try:
        patient = Patient.objects.create(**data)
        patient.save()
    except Exception as e:
        messages.error(request, f'{e}')



