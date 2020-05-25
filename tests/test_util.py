import pytest
from python_debug import util


def test_get_path():
    head = util.get_path("test_python_debug.py")
    # assert head == "kitten", "Incorrect path"
    assert head == "", "Incorrect path"


def test_get_path_exceptions():
    """ Check if the function raises correct exception """
    with pytest.raises(TypeError):
        # util.get_path("one")
        util.get_path(1)
