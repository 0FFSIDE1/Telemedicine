from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.patient_services import *
# Create your views here.

class PatientView(APIView):
    def get(self, request):
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        data = {
            'status': 'success',
            'message': 'Patient data retrieved successfully',
            'patients': serializer.data,  
        }
        return Response(data=data, status=status.HTTP_200_OK)