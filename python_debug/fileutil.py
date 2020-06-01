import os


def get_path(filename):
    """
    Return the path of the file
    args:
        filename (str): name of the file
    returns:
        head (str): path to the file
    """
    breakpoint()
    if type(filename) != str:
        raise TypeError
    head, tail = os.path.split(filename)  # pylint: disable=unused-variable
    return head
