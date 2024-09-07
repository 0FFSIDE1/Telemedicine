from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/ed_visits', AllEd_visitsView.as_view(), name='all-ed_visits'),
    path('api/v1/<int:pk>/ed_visit', Ed_visitsDetailView.as_view(), name='ed_visit-detail'),
    
]