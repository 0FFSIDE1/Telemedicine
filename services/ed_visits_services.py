from rest_framework import serializers
from ed_visits.models import Ed_visit
class Ed_visitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ed_visit
        fields = "__all__"
                    
def All_Ed_visits_Response_data(ed_visits, queryset):
    """Response Data for GET request i.e all ed_visits record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "List of all ed_visits retrieved successfully.",
        "count": queryset,
        "ed_visits": ed_visits,
    }
    return data

def Create_Ed_visits_Response_data(ed_visit, headers):
    """Response Data for POST request i.e create new ed_visit record"""
    data = {
        "status": "success",
        "code": 201,
        "message": "ed_visit record added successfully.",
        "ed_visit": ed_visit,
    }
    header = headers
    return (data, header)

def Retrieve_Ed_visits_Response_data(ed_visit):
    """Response Data for GET request i.e single ed_visit record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "ed_visit record retrieved successfully.",
        "ed_visit": ed_visit,
    }
    return data

def Update_Ed_visits_Response_data(ed_visit):
    """Response Data for PUT or PATCH request i.e update single ed_visit record"""
    data = {
        "status": "success",
        "code": 200,
        "message": "ed_visit record updated successfully.",
        "ed_visit": ed_visit,
    }
    return data

def Destroy_Ed_visits_Response_data():
    """Response Data for Delete request i.e Delete single ed_visit record"""
    data = {
        "status": "success",
        "code": 204,
        "message": "ed_visit record deleted successfully.",
    }
    return data
    
    