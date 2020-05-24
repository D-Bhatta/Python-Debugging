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


