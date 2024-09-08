from django.http import Http404
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.admission_services import *
from services.error_response import Error_Response
from admissions.models import Admission
from rest_framework import generics
from rest_framework.exceptions import NotFound

# Create your views here.
class AllAdmissionView(generics.ListCreateAPIView):
    """
       GET: Retrieves all Admission record
       POST: Add new Admission record
       queryset: All column in Admission Entity
       serializer_class: All rows in Admission Entity
    """
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    # GET
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(All_admission_Response_data(
            queryset = queryset.count(), 
            admission = serializer.data),
        )
    
    # POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(Create_admission_Response_data(
            admission = serializer.data,      
        ), status = status.HTTP_201_CREATED)
    
    
class AdmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       GET: Retrieves specific admission record
       PUT and PATCH: update specific admission record
       DELETE: delete specific admission record
       queryset: all column in admission Entity
       serializer_class: All rows in Admission Entity
    """
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail=Error_Response, code=404)
    
    # GET
    def retrieve(self, request, *args, **kwargs):
        admission = self.get_object()
        serializer = self.get_serializer(admission)
        return Response(Retrieve_admission_Response_data(
            admission = serializer.data,
        ), status=status.HTTP_200_OK)

    # Update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(Update_admission_Response_data(
            admission = serializer.data,
        ), status=status.HTTP_200_OK)
    
    # Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(Destroy_admission_Response_data(), 
                        status=status.HTTP_204_NO_CONTENT)
       