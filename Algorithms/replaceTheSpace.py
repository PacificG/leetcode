def replaceSpace(string):
    """
    Replace a space in a string with "%20.
    >>> replaceSpace("A B")
    'A%20B'
    """
    return string.replace(" ", "%20")
