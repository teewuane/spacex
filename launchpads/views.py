"""Views for the launchpads app."""
from rest_framework import viewsets
from launchpads.serializers import LaunchpadSerializer
from launchpads.launchpads import launchpads
from rest_framework.response import Response


class LaunchpadViewSet(viewsets.ViewSet):
    """API endpoint that consumes the spacex endpoint."""

    serializer_class = LaunchpadSerializer

    def list(self, request):
        """The list view."""
        serializer = LaunchpadSerializer(
            instance=launchpads.values(), many=True)

        return Response(serializer.data)
