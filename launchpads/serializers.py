"""Serializers for the launchpads app."""
from rest_framework import serializers


class LaunchpadSerializer(serializers.Serializer):
    """Data Serializer."""

    # See launchpads.py for available fields.
    id = serializers.CharField(read_only=True, max_length=256)
    full_name = serializers.CharField(max_length=256)
    status = serializers.CharField(max_length=256)

    # These are not implemented.
    # def create(self, validated_data):
    #     """Create method."""
    #     return LaunchpadSerializer(id=None, **validated_data)

    # def update(self, instance, validated_data):
    #     """Update method."""
    #     for field, value in validated_data.items():
    #         setattr(instance, field, value)
    #     return instance
