from django.http import Http404
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.patient_services import *
from rest_framework import generics
from rest_framework.exceptions import NotFound
# Create your views here.

class AllPatientView(generics.ListCreateAPIView):
        """
        GET: Retrieves all patients record
        POST: Add new patient record
        queryset: All column in Patient Entity
        serializer_class: All rows in patient Entity
        """
        queryset = Patient.objects.all()
        serializer_class = PatientSerializer
        
        # GET
        def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(All_Patient_Response_data(
                queryset = queryset.count(), 
                patient = serializer.data),
            )

        # POST
        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(Create_Patient_Response_data(
                patient = serializer.data,
                headers = self.get_success_headers(serializer.data),      
            ), status = status.HTTP_201_CREATED)
       
class PatientView(generics.RetrieveUpdateDestroyAPIView):
    """
       GET: Retrieves specific patient record
       PUT and PATCH: update specific patient record
       DELETE: delete specific patient record
       queryset: all column in Patient Entity
       serializer_class: All rows in patient Entity
    """
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

    # GET
    def retrieve(self, request, *args, **kwargs):
        patient = self.get_object()
        serializer = self.get_serializer(patient)
        return Response(Retrieve_Patient_Response_data(
            patient = serializer.data,
        ), status=status.HTTP_200_OK)

    # Update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(Update_Patient_Response_data(
            patient = serializer.data,
        ), status=status.HTTP_200_OK)
    
    # Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(Destroy_Patient_Response_data(), 
                        status=status.HTTP_204_NO_CONTENT)
       


   