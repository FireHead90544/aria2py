import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)
from aria2py import Aria2Client

aria2 = Aria2Client("localhost", 6800)


def test_get_version():
    """
    Tests the get_version method of the Aria2Client class.
    """
    assert (
        "version" in aria2.get_version(raw=True)["result"]
    ), "Expected key 'version' in response. Check connection/credentials."
    assert isinstance(
        aria2.get_version(), str
    ), "Expected string response. Check server connection/credentials."
