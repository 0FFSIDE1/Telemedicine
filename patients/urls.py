from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/patients', PatientView.as_view(), name='all-patient')
]