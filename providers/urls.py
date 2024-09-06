from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/providers', AllProvidersView.as_view(), name='all-provider'),
    path('api/v1/<int:pk>/provider', ProviderDetailView.as_view(), name='provider-detail'),
    
]