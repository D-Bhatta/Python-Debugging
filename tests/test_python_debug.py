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


def test_example_3(capsys):
    python_debug.example_3()
    captured = capsys.readouterr()
    assert "python_debug" in captured.out


def test_example_4(capsys):
    python_debug.example_4()
    captured = capsys.readouterr()
    assert "python_debug" in captured.out


def test_example_5(capsys):
    python_debug.example_5()
    captured = capsys.readouterr()
    assert "python_debug" in captured.out


def test_get_path_fname():
    head = python_debug.get_path_fname("test_python_debug.py")
    assert head == "", "Incorrect path"


def test_get_path_fname_exception():
    """ Check if the function raises correct exception """
    with pytest.raises(TypeError):
        python_debug.get_path_fname(1)


def test_example_6(capsys):
    python_debug.example_6()
    captured = capsys.readouterr()
    assert "python_debug" in captured.out


def test_get_file_info():
    file_path = python_debug.get_file_info("test_python_debug.py")
    assert file_path == "", "Incorrect path"


def test_get_file_info_exception():
    """ Check if the function raises correct exception """
    with pytest.raises(TypeError):
        python_debug.get_file_info(1)
