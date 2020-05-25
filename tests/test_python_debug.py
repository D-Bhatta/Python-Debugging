""" Tests for 'python_debug' package """

import pytest

from python_debug import python_debug


def test_hello_world(capsys):
    """ Correct object argument prints """
    python_debug.helloworld("python")
    captured = capsys.readouterr()
    assert "python" in captured.out


def test_helloworld_exception():
    """ Check if the function raises correct exception """
    with pytest.raises(TypeError):
        python_debug.helloworld(1)


def test_example_1(capsys):
    """ Check if correct filename prints """
    python_debug.example_1()
    captured = capsys.readouterr()
    assert "python_debug" in captured.out


def test_get_path_exceptions():
    """ Check if the function raises correct exception """
    with pytest.raises(TypeError):
        python_debug.get_path(1)


def test_get_path():
    head = python_debug.get_path("test_python_debug.py")
    assert head == "", "Incorrect path"


def test_example_2(capsys):
    python_debug.example_2()
    captured = capsys.readouterr()
    assert "python_debug" in captured.out
