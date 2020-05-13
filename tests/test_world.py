"""Test the world module."""

import datetime

from pygohome.world import World


def test_no_trackpoints():
    """Fresh world contains no trackpoints."""
    world = World()
    assert not world._trackpoints
    assert not world._checked


def test_one_trackpoint():
    """Fresh world with one trackpoint."""
    world = World()
    world.add_trackpoints(
        [(datetime.datetime(2020, 5, 1, 12, 0, 0, 0, datetime.timezone.utc), 49.0, 8.4)]
    )
    assert len(world._trackpoints) == 1
    assert not world._checked
