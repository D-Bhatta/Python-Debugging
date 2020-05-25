import os

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
