from django.conf import settings
from rest_framework import serializers
from .models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):
    """Serializer for short urls objects"""
    class Meta:
        model = ShortURL
        fields = ['id', 'original_url', 'short_code']
        read_only_fields = ('id', 'short_code')

    def to_representation(self, instance):
        """Return the short URL with the BASE_URL"""
        data = super().to_representation(instance)
        data['short_url'] = f"{settings.BASE_URL}/{instance.short_code}"
        return data
