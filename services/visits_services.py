from rest_framework import serializers
from visits.models import Visit

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ["visit_id",
            "date_of_visit",
            "date_scheduled",
            "visit_department_id",
            "visit_type",
            "blood_pressure_systolic",
            "blood_pressure_diastolic",
            "pulse",
            "visit_status",
            "patient",
            "provider",]
    
