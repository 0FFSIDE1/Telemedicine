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
        # GET
        def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(All_Provider_Response_data(
                queryset = queryset.count(), 
                provider = serializer.data),
            )

        # POST
        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(Create_Provider_Response_data(
                provider = serializer.data,
                headers = self.get_success_headers(serializer.data),      
            ), status = status.HTTP_201_CREATED)
       
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

    # GET
    def retrieve(self, request, *args, **kwargs):
        provider = self.get_object()
        serializer = self.get_serializer(provider)
        return Response(Retrieve_Provider_Response_data(
            provider = serializer.data,
        ), status = status.HTTP_200_OK)

    # Update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(Update_Provider_Response_data(
            provider = serializer.data,
        ), status=status.HTTP_200_OK)
    
    # Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(Destroy_Provider_Response_data(), 
                        status=status.HTTP_204_NO_CONTENT)

