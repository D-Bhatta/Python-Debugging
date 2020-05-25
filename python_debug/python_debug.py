import os
from python_debug import util

# pylint: disable=anomalous-backslash-in-string
def helloworld(code):
    """ 
    Print a line 
    args:
        code (str): name of the code
    returns:
        None
    """
    if type(code) != str:
        raise TypeError

    print("I am a {}.".format(code))


def example_1():
    """ 
    output:
    > j:\education\code\python\python-debugging\python_debug\python_debug.py(17)example_1()
    -> print(f'path = {filename}')
    (Pdb) p filename
    'python_debug.py'
    """
    filename = __file__
    breakpoint()
    print(f"path = {filename}")


def get_path(filename):
    """
    Return the path of the file
    args:
        filename (str): name of the file
    returns:
        head (str): path to the file
    """
    if type(filename) != str:
        raise TypeError
    head = os.path.split(filename)[0]
    return head


def example_2():
    filename = __file__
    print(f"path  = {get_path(filename)}")


def example_3():
    filename = __file__
    breakpoint()
    filename_path = get_path(filename)
    print(f"path = {filename_path}")


def example_4():
    filename = __file__
    breakpoint()
    filename_path = util.get_path(filename)
    print(f"path = {filename_path}")


def get_path_fname(fname):
    """ 
    Return the path of the file
    args:
        fname (str): name of the file
    returns:
        head (str): path to the file
    """
    breakpoint()
    if type(fname) != str:
        raise TypeError
    head, tail = os.path.split(fname)  # pylint: disable=unused-variable
    for char in tail:
        pass
    return head


def example_5():
    filename = __file__
    filename_path = get_path_fname(filename)
    print(f"path = {filename_path}")


example_5()
