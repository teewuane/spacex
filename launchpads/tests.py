"""Tests for the launchpads app."""

from django.test import TestCase
from launchpads.launchpads import Launchpad


class TestLaunchpad(TestCase):
    """Test creating a new Launchpad instance."""

    def test_status(self):
        """Ensure that testpad knows its status."""
        testpad = Launchpad(id='testid', full_name='testname', status='teststatus')
        self.assertEqual(testpad.say_status(), "My status is 'teststatus'.")
        self.assertEqual(testpad.say_name(), "My name is 'testname'.")
        self.assertEqual(testpad.say_id(), "My id is 'testid'.")
