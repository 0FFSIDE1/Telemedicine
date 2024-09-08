from rest_framework import serializers
from admissions.models import Admission

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'
    
def All_admission_Response_data(admission, queryset):
    """Response Data for GET request i.e all admission record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "List of all admissions retrieved successfully.",
        "count": queryset,
        "admissions": admission,
    }
    return data

def Create_admission_Response_data(admission):
    """Response Data for POST request i.e create new admission record"""
    data = {
        "status": "success",
        "code": 201,
        "message": "admission record added successfully.",
        "admission": admission,
    }
    
    return data

def Retrieve_admission_Response_data(admission):
    """Response Data for GET request i.e single admission record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "Admission record retrieved successfully.",
        "admission": admission,
    }
    return data

def Update_admission_Response_data(admission):
    """Response Data for PUT or PATCH request i.e update single admission record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "admission record updated successfully.",
        "admission": admission,
    }
    return data

def Destroy_admission_Response_data():
    """Response Data for Delete request i.e Delete single admission record"""
    data = {
        "status": "success",
        "code": 204,
        "message": "admission record deleted successfully.",
    }
    return data




