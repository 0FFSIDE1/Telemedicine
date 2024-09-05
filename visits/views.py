from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.visits_services import *
from visits.models import Visit
from rest_framework import generics
from rest_framework.exceptions import NotFound

# Create your views here.
class AllVisitsView(APIView):
    def get(self, request):
        visit = Visit.objects.all()
        serializer = VisitSerializer(visit, many=True)
        data = {
            'status': 'success',
            'message': 'All Visitation data retrieved successfully',
            'patients': serializer.data,  
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
class VisitView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    def get_object(self):
       try:
           return super().get_object()
       except Http404:
           raise NotFound(detail="Visit record not found with the provided ID.", code=404)
       