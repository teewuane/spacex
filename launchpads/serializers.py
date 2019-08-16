"""Serializers for the launchpads app."""
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Model Serializer."""

    class Meta:
        """Meta."""

        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Model Serializer."""

    class Meta:
        """Meta."""

        model = Group
        fields = ['url', 'name']

STATUSES = [
    'Open',
    'Closed',
]


class LaunchpadSerializer(serializers.Serializer):
    """Data Serializer."""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)
    status = serializers.ChoiceField(choices=STATUSES, default='Open')

    def create(self, validated_data):
        """Create method."""
        return LaunchpadSerializer(id=None, **validated_data)

    def update(self, instance, validated_data):
        """Update method."""
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
