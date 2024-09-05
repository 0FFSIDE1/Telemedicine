from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from patients.models import Patient
from visits.models import Visit
from django.contrib import messages
from .visits_services import VisitSerializer
from rest_framework import status


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    
class PatientVisitSerializer(serializers.ModelSerializer):
    visits = serializers.SerializerMethodField()
    class Meta:
        model = Visit
        fields = '__all__'
    def get_patient_visits(self, obj):
        visits = Visit.objects.filter(patient=obj)
        return VisitSerializer(visits)

def create_patient_record(request, data):
    try:
        patient = Patient.objects.create(**data)
    except Exception as e:
        messages.error(request, f'{e}')



    

