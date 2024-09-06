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
    
class PatientVisitSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Visit
        fields = [
            'visit_id', 
            'date_of_visit',
            'date_scheduled',
            'visit_department_id', 
            'visit_type', 
            'blood_pressure_systolic', 
            'blood_pressure_diastolic', 
            'pulse', 
            'visit_status', 
            'patient', 
            'provider', 
        ]

def create_patient_record(request, data):
    try:
        patient = Patient.objects.create(**data)
        patient.save()
    except Exception as e:
        messages.error(request, f'{e}')



