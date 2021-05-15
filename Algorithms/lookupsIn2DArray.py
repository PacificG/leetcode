def lookup(matrix, num):
    """
    Given a two-dimensional array, each row is sorted incrementally from left
    to right, and from top to bottom is also incremental. Given a number,
    determine whether the number is in the two-dimensional array.
    >>> A = [[1, 4, 7, 11, 15],[2, 5, 8, 12, 19],[3, 6, 9, 16, 22]]
    >>> lookup(A, 5)
    True
    >>> lookup(A, 20)
    False
    """
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols - 1
    while r <= rows - 1 and c >= 0:
        if num == matrix[r][c]:
            return True
        elif num > matrix[r][c]:
            r += 1
        else:
            c -= 1
    return False
