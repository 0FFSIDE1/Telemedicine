from django.http import Http404
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.provider_services import *
from rest_framework import generics
from rest_framework.exceptions import NotFound
# Create your views here.

class AllProvidersView(generics.ListCreateAPIView):
        """
        GET: Retrieves all provider record
        POST: Add new provider record
        queryset: All column in Provider Entity
        """
        queryset = Provider.objects.all()
        serializer_class = ProviderSerializer
       
class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
       GET: Retrieves specific provider record
       PUT and PATCH: update provider record
       DELETE: delete specific provider record
       queryset: all column in Provider Entity
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Provider not found with the provided ID.", code=404)
       
    # def check_permissions(self, request):
    #     if not request.user.has_perm('patients.change_Patient'):
    #         raise PermissionDenied({"error": "You do not have permission to update this object."})
    #     return super().check_permissions(request)

