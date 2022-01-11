# api/serializers.py

from rest_framework import serializers
from core.models import Asset

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ('name', 'symbol', 'description')