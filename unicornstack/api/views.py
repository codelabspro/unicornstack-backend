from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from rest_framework import viewsets
from rest_framework.utils import serializer_helpers
from .serializers import AssetSerializer
from core.models import Asset

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('name')
    serializer_class = AssetSerializer
def getCustomRoutes(request):
    routes = [
        {
            'Endpoint': '/assets/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of assets'
        },
        {
            'Endpoint': '/assets/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single asset' 
        },
        {
            'Endpoint': '/assets/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new asset with data sent in post request'
        },
        {
            'Endpoint': '/assets/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing asset' 
        },
    ]
    return JsonResponse(routes, safe=False)