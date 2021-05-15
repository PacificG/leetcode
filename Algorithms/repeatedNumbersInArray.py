def repeatedNumbers(list):
    """
    All numbers in an array of n lengths are in the range of 0 to n-1. Some
    numbers in the array are duplicates, but it is not known how many numbers
    are duplicates, or how many times each number is repeated. Find any
    duplicate number in the array.
    >>> repeatedNumbers([2,3,1,0,2,5])
    2
    """
    for i in range(len(list)):
        while list[i] != i:
            if list[i] == list[list[i]]:
                return list[i]
            swap(list, i, list[i])
        swap(list, i, list[i])
    return -1


def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
