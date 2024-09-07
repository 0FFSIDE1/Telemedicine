from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/discharges', AllDischargeView.as_view(), name='all-discharges'),
    path('api/v1/<int:pk>/discharge', DischargeDetailView.as_view(), name='discharge-detail'),
    
]