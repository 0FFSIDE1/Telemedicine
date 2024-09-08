from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from patients.models import Patient
from django.contrib import messages
from rest_framework import status

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    

def All_Patient_Response_data(patient, queryset):
    """Response Data for GET request i.e all patient record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "List of all patients retrieved successfully.",
        "count": queryset,
        "patients": patient,
    }
    return data

def Create_Patient_Response_data(patient):
    """Response Data for POST request i.e create new patient record"""
    data = {
        "status": "success",
        "code": 201,
        "message": "Patient record added successfully.",
        "patient": patient,
    }
    
    return data

def Retrieve_Patient_Response_data(patient):
    """Response Data for GET request i.e single patient record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "Patient record retrieved successfully.",
        "patient": patient,
    }
    return data

def Update_Patient_Response_data(patient):
    """Response Data for PUT or PATCH request i.e update single patient record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "Patient record updated successfully.",
        "patient": patient,
    }
    return data

def Destroy_Patient_Response_data():
    """Response Data for Delete request i.e Delete single patient record"""
    data = {
        "status": "success",
        "code": 204,
        "message": "Patient record deleted successfully.",
    }
    return data


