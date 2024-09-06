from django.http import Http404
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.visits_services import *
from services.patient_services import PatientVisitSerializer
from visits.models import Visit
from rest_framework import generics
from rest_framework.exceptions import NotFound

# Create your views here.
class AllVisitsView(generics.ListCreateAPIView):
    """
       GET: Retrieves all visits record
       POST: Add new visit record
       queryset: All column in visit Entity
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    
    
class VisitView(generics.RetrieveUpdateDestroyAPIView):
    """
       GET: Retrieves specific visits record
       PUT and PATCH: update visit record
       DELETE: delete specific visit record
       queryset: all column in visit Entity
    """
    queryset = Visit.objects.all()
    serializer_class = PatientVisitSerializer
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Visit record not found with the provided ID.", code=404)
       