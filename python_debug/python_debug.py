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
    import pdb; pdb.set_trace()
    print(f'path = {filename}')

example_1()
