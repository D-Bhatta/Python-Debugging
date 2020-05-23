""" Tests for 'python_debug' package """

import pytest

from python_debug import python_debug


def test_hello_world(capsys):
    """ Correct object argument prints """
    python_debug.helloworld("python")
    captured = capsys.readouterr()
    assert "python" in captured.out


def test_helloworld_exception():
    with pytest.raises(TypeError):
        python_debug.helloworld(1)
