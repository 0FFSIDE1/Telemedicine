from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.patient_services import *
from rest_framework import generics
from rest_framework.exceptions import NotFound
# Create your views here.

class AllPatientView(APIView):
    def get(self, request):
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        data = {
            'status': 'success',
            'message': 'All Patients data retrieved successfully',
            'patients': serializer.data,  
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
class PatientView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_object(self):
       try:
           return super().get_object()
       except Http404:
           raise NotFound(detail="Patient not found with the provided ID.", code=404)
       
    # def check_permissions(self, request):
    #     if not request.user.has_perm('patients.change_Patient'):
    #         raise PermissionDenied({"error": "You do not have permission to update this object."})
    #     return super().check_permissions(request)
   