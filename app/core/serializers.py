from rest_framework import serializers
from .models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):
    """Serializer for short urls objects"""
    class Meta:
        model = ShortURL
        fields = ['id', 'original_url', 'short_code']
        read_only_fields = ('id', 'short_code')
