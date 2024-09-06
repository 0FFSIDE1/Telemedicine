from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/providers', AllProviderView.as_view(), name='all-provider'),
    path('api/v1/<int:pk>/provider', ProviderView.as_view(), name='provider'),
    
]