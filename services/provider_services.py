from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from providers.models import Provider
from visits.models import Visit
from django.contrib import messages

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
    
                    
def All_Provider_Response_data(provider, queryset):
    """Response Data for GET request i.e all provider record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "List of all provider retrieved successfully.",
        "count": queryset,
        "providers": provider,
    }
    return data

def Create_Provider_Response_data(provider, headers):
    """Response Data for POST request i.e create new provider record"""
    data = {
        "status": "success",
        "code": 201,
        "message": "provider record added successfully.",
        "provider": provider,
    }
    header = headers
    return (data, header)

def Retrieve_Provider_Response_data(provider):
    """Response Data for GET request i.e single provider record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "provider record retrieved successfully.",
        "provider": provider,
    }
    return data

def Update_Provider_Response_data(provider):
    """Response Data for PUT or PATCH request i.e update single provider record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "provider record updated successfully.",
        "provider": provider,
    }
    return data

def Destroy_Provider_Response_data():
    """Response Data for Delete request i.e Delete single provider record"""
    data = {
        "status": "success",
        "code": 204,
        "message": "provider record deleted successfully.",
    }
    return data
    
    
