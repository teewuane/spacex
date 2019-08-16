"""
I'll replace this with a django model later.

For now I'll mock some data.

Then I'll hook up to the spacex api.

Then I'll cache the requests and stick them in redis so I don't hammer the SpaceX API.
"""


class Launchpad(object):
    """Represent data that is not in a model."""

    def __init__(self, **kwargs):
        """Init the class."""
        for field in ['id', 'name', 'owner', 'status']:
            setattr(self, field, kwargs.get(field, None))


launchpads = {
    1: Launchpad(id=1, name='Hello', owner='teewuane', status='Open'),
    2: Launchpad(id=2, name='Model less', owner='someone', status='Closed'),
    3: Launchpad(id=3, name='Sleep', owner='teewuane', status='Closed'),
}
