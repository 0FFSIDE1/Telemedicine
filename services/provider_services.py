from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from providers.models import Provider
from visits.models import Visit
from django.contrib import messages

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
    





