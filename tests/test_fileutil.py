import pytest
from python_debug import fileutil


def test_get_path():
    head = fileutil.get_path("test_python_debug.py")
    assert head == "", "Incorrect path"
    # assert head == "", "Incorrect path"


def test_get_path_exceptions():
    """ Check if the function raises correct exception """
    with pytest.raises(TypeError):
        fileutil.get_path(1)
        # fileutil.get_path(1)
