from rest_framework import serializers
from visits.models import Visit

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"
                    
def All_Visit_Response_data(visit, queryset):
    """Response Data for GET request i.e all visits record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "List of all patients visits retrieved successfully.",
        "count": queryset,
        "visits": visit,
    }
    return data

def Create_Visit_Response_data(visit, headers):
    """Response Data for POST request i.e create new visit record"""
    data = {
        "status": "success",
        "code": 201,
        "message": "Visit record added successfully.",
        "visits": visit,
    }
    header = headers
    return (data, header)

def Retrieve_Visit_Response_data(visit):
    """Response Data for GET request i.e single visit record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "Visit record retrieved successfully.",
        "visits": visit,
    }
    return data

def Update_Visit_Response_data(visit):
    """Response Data for PUT or PATCH request i.e update single visit record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "Visit record updated successfully.",
        "visits": visit,
    }
    return data

def Destroy_Visit_Response_data():
    """Response Data for Delete request i.e Delete single visit record"""
    data = {
        "status": "success",
        "code": 204,
        "message": "Visit record deleted successfully.",
    }
    return data
    
    