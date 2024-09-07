from django.http import Http404
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.discharge_services import *
from discharges.models import Discharge
from rest_framework import generics
from rest_framework.exceptions import NotFound

# Create your views here.
class AllDischargeView(generics.ListCreateAPIView):
    """
       GET: Retrieves all discharge record
       POST: Add new discharge record
       queryset: All column in discharge Entity
    """
    queryset = Discharge.objects.all()
    serializer_class = DischargeSerializer
    
    # GET
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(All_Discharge_Response_data(
            queryset = queryset.count(), 
            discharge = serializer.data),
            status = status.HTTP_200_OK,
        )
    
    # POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(Create_Discharge_Response_data(
            discharge = serializer.data,
            headers = self.get_success_headers(serializer.data),      
        ), status = status.HTTP_201_CREATED)
    
    
class DischargeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       GET: Retrieves specific discharge record
       PUT and PATCH: update discharge record
       DELETE: delete/destroy specific discharge record
       queryset: all column in discharge Entity
    """
    queryset = Discharge.objects.all()
    serializer_class = DischargeSerializer
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Discharge record not found with the provided ID.", code=404)
    
    # GET
    def retrieve(self, request, *args, **kwargs):
        discharge = self.get_object()
        serializer = self.get_serializer(discharge)
        return Response(Retrieve_Discharge_Response_data(
            discharge = serializer.data,
        ), status=status.HTTP_200_OK)

    # Update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(Update_Discharge_Response_data(
            discharge = serializer.data,
        ), status = status.HTTP_200_OK)
    
    # Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(Destroy_Discharge_Response_data(), 
                        status = status.HTTP_204_NO_CONTENT)
       