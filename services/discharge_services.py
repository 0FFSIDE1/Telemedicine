from rest_framework import serializers
from discharges.models import Discharge

class DischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discharge
        fields = "__all__"
                    
def All_Discharge_Response_data(discharge, queryset):
    """Response Data for GET request i.e all discharge record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "List of all patients Discharges retrieved successfully.",
        "count": queryset,
        "discharges": discharge,
    }
    return data

def Create_Discharge_Response_data(discharge, headers):
    """Response Data for POST request i.e create new Discharge record"""
    data = {
        "status": "success",
        "code": 201,
        "message": "Discharge record added successfully.",
        "discharge": discharge,
    }
    header = headers
    return (data, header)

def Retrieve_Discharge_Response_data(discharge):
    """Response Data for GET request i.e single Discharge record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "Discharge record retrieved successfully.",
        "discharge": discharge,
    }
    return data

def Update_Discharge_Response_data(discharge):
    """Response Data for PUT or PATCH request i.e update single Discharge record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "Discharge record updated successfully.",
        "discharge": discharge,
    }
    return data

def Destroy_Discharge_Response_data():
    """Response Data for Delete request i.e Delete single Discharge record"""
    data = {
        "status": "success",
        "code": 204,
        "message": "Discharge record deleted successfully.",
    }
    return data
    
    