"""Views for the launchpads app."""
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from launchpads.serializers import (
    UserSerializer,
    GroupSerializer,
    LaunchpadSerializer)
from launchpads.launchpads import launchpads
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LaunchpadViewSet(viewsets.ViewSet):
    """API endpoint that consumes the spacex endpoint."""

    serializer_class = LaunchpadSerializer

    def list(self, request):
        """The list view."""
        serializer = LaunchpadSerializer(
            instance=launchpads.values(), many=True)

        return Response(serializer.data)
