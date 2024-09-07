from django.http import Http404
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.visits_services import *
from visits.models import Visit
from rest_framework import generics
from rest_framework.exceptions import NotFound

# Create your views here.
class AllVisitsView(generics.ListCreateAPIView):
    """
       GET: Retrieves all visits record
       POST: Add new visit record
       queryset: All column in visit Entity
       serializer_class: All rows in visit Entity
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    
    # GET
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(All_Visit_Response_data(
            queryset=queryset.count(), 
            visit=serializer.data),
        )
    
    # POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(Create_Visit_Response_data(
            visit = serializer.data,
            headers = self.get_success_headers(serializer.data),      
        ), status = status.HTTP_201_CREATED)
    
    
class VisitDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       GET: Retrieves specific visits record
       PUT and PATCH: update visit record
       DELETE: delete specific visit record
       queryset: all column in visit Entity
       serializer_class: All rows in visit Entity
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Visit record not found with the provided ID.", code=404)
    
    # GET
    def retrieve(self, request, *args, **kwargs):
        visit = self.get_object()
        serializer = self.get_serializer(visit)
        return Response(Retrieve_Visit_Response_data(
            visit = serializer.data,
        ), status=status.HTTP_200_OK)

    # Update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(Update_Visit_Response_data(
            visit = serializer.data,
        ), status=status.HTTP_200_OK)
    
    # Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(Destroy_Visit_Response_data(), 
                        status=status.HTTP_204_NO_CONTENT)
       