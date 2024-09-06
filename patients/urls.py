from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/patients', AllPatientView.as_view(), name='all-patient'),
    path('api/v1/<int:pk>/patient', PatientView.as_view(), name='patient-detail'),
    
]