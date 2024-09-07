from django.http import Http404
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.ed_visits_services import *
from ed_visits.models import Ed_visit
from rest_framework import generics
from rest_framework.exceptions import NotFound

# Create your views here.
class AllEd_visitsView(generics.ListCreateAPIView):
    """
       GET: Retrieves all ed_visits record
       POST: Add new ed_visits record
       queryset: All column in ed_visits Entity
       serializer_class: All rows in ed_visits Entity
    """
    queryset = Ed_visit.objects.all()
    serializer_class = Ed_visitsSerializer
    
    # GET
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(All_Ed_visits_Response_data(
            queryset = queryset.count(), 
            ed_visits = serializer.data),
            status = status.HTTP_200_OK,
        )
    
    # POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(Create_Ed_visits_Response_data(
            ed_visit = serializer.data,
            headers = self.get_success_headers(serializer.data),      
        ), status = status.HTTP_201_CREATED)
    
    
class Ed_visitsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       GET: Retrieves specific ed_visits record
       PUT and PATCH: update ed_visit record
       DELETE: delete/destroy specific ed_visit record
       queryset: all column in ed_visit Entity
       serializer_class: All rows in ed_visits Entity
    """
    queryset = Ed_visit.objects.all()
    serializer_class = Ed_visitsSerializer
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Ed_visits record not found with the provided ID.", code=404)
    
    # GET
    def retrieve(self, request, *args, **kwargs):
        ed_visit = self.get_object()
        serializer = self.get_serializer(ed_visit)
        return Response(Retrieve_Ed_visits_Response_data(
           ed_visit = serializer.data,
        ), status=status.HTTP_200_OK)

    # Update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(Update_Ed_visits_Response_data(
            ed_visit = serializer.data,
        ), status = status.HTTP_200_OK)
    
    # Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(Destroy_Ed_visits_Response_data(), 
                        status = status.HTTP_204_NO_CONTENT)
       