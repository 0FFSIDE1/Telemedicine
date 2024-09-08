from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/admissions', AllAdmissionView.as_view(), name='all-admissions'),
    path('api/v1/<int:pk>/admission', AdmissionDetailView.as_view(), name='admission-detail'),
    
]