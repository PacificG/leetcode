def printClockwise(matrix):
    """
    Print the value of the matrix from outside to inside in a clockwise
    direction.
    >>> A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> printClockwise(A)
    '1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10'
    """
    strings = []
    r1, r2, c1, c2 = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for i in range(c1, c2+1):
            strings.append(matrix[r1][i])
        for i in range(r1+1, r2+1):
            strings.append(matrix[i][c2])
        if r1 != r2:
            for i in range(c2-1, c1-1, -1):
                strings.append(matrix[r2][i])
        if c1 != c2:
            for i in range(r2-1, r1, -1):
                strings.append(matrix[i][c1])
        r1, r2, c1, c2 = r1 + 1, r2 - 1, c1 + 1, c2 - 1
    return ", ".join([str(s) for s in strings])
