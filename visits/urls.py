from django.urls import path
from .views import *
urlpatterns = [
    path('api/v1/visitation', AllVisitsView.as_view(), name='all-visits'),
    path('api/v1/<int:pk>/visitation', VisitView.as_view(), name='visit-detail')
]
    