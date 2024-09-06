from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from providers.models import Provider
from visits.models import Visit
from django.contrib import messages

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
    
class ProviderVisitSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()
    class Meta:  
        model = Visit
        fields = ['visit_id', 'date_of_visit', 'date_scheduled', 'visit_department_id', 'visit_type', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'pulse', 'visit_status', 'patient', 'provider', ]
    def get_patient(self, obj):
        return obj.patient.first_name
    def get_provider(self, obj):
        return obj.provider.first_name

def create_patient_record(request, data):
    try:
        provider = Provider.objects.create(**data)
        provider.save()
    except Exception as e:
        messages.error(request, f'{e}')



