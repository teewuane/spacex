"""
I'll replace this with a django model later.

For now I'll mock some data.

Then I'll hook up to the spacex api.

Then I'll cache the requests and stick them in redis so I don't hammer the SpaceX API.
"""
import requests


class Launchpad(object):
    """Represent data that is not in a model."""

    # This class could easily be replaced by a django model using the django rest framework.
    def __init__(self, **kwargs):
        """Init the class."""
        # self.pad_id = kwargs.get('padid', None)
        self.id = kwargs.get('id', None)
        self.full_name = kwargs.get('full_name', None)
        self.status = kwargs.get('status', None)

    def say_status(self):
        """Used for testing."""
        return "My status is '%s'." % (self.status)

    def say_name(self):
        """Used for testing."""
        return "My name is '%s'." % (self.full_name)

    def say_id(self):
        """Used for testing."""
        return "My id is '%s'." % (self.id)


def fetch_launchpads():
    """Request launchpads from spacex api."""
    r = requests.get("https://api.spacexdata.com/v2/launchpads")

    launchpads = {}

    for idx, item in enumerate(r.json()):
        launchpads[idx] = item

    return launchpads

    # return {
    #     1: Launchpad(id=1, full_name='Hello', status='Open'),
    #     2: Launchpad(id=2, full_name='Model less', status='Closed'),
    #     3: Launchpad(id=3, full_name='Sleep', status='Closed'),
    # }

launchpads = fetch_launchpads()
