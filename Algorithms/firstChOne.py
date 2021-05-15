def firstCharacterOnlyOnce(string):
    """
    Find the first character in a string that appears only once and return its
    position. Strings contain only ASCII code characters.
    >>> firstCharacterOnlyOnce("abacc")
    'b'
    """
    from collections import Counter
    dic = Counter(string)
    for d in dic:
        if dic[d] == 1:
            return d
    return -1
