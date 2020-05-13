"""Test the convert module."""

from pathlib import Path
import pytest

import pygohome.convert as conv


@pytest.mark.parametrize(
    "filename", ["emptyfile", "hello_world.txt", "osmand_invalid.gpx"]
)
def test_gpx_invalid_file_fails(filename):
    """Expect an error when reading non-GPX-XML files."""
    content = (Path("tests/testdata") / filename).read_text()
    with pytest.raises(conv.InvalidFileError):
        conv.gpx_to_trackpoints(content)


def test_gpx_no_points():
    """Read a valid GPX file with no trackpoints in it."""
    content = Path("tests/testdata/osmand_nopoints.gpx").read_text()
    assert conv.gpx_to_trackpoints(content) == []
