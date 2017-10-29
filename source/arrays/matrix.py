"""


[title]: # (Операции с матрицами)


Операции с матрицами
============================

Матрично - векторное умножение

    >>> A = [[2, 3],
    ...      [1, 2]]
    >>> B = [1, 2]
    >>> S = [0 for _ in range(len(B))]
    >>> for i in range(len(A)):
    ...     for j in range(len(B)):
    ...         S[i] += A[i][j] * B[j]
    >>> S
    [8, 5]

Векторно - матричное умножение

    >>> A = [1, 2]
    >>> B = [[2, 3],
    ...      [1, 2]]
    >>> S = [0 for _ in range(len(A))]
    >>> for j in range(len(A)):
    ...     for i in range(len(B)):
    ...         S[j] += A[i] * B[i][j] 
    >>> S
    [4, 7]

Перемножение строки на столбец

    >>> A = [[2, 4]]
    >>> B = [[.5],
    ...      [.5]]

    >>> s = 0
    >>> for row in range(len(A)):
    ...     for col in range(len(A[row])):
    ...         s += A[row][col] * B[col][row]


Перемножение двух матриц n x n
    
    >>> A = [[2,  2], 
    ...      [4,  4],
    ...      [6,  6]]
    >>> B = [[1,  1],
    ...      [2,  2]]

    >>> C = []
    >>> for i in range(len(A)):
    ...     c = [0 for j in range(len(B))]
    ...     C.append(c)
    
    >>> for i in range(len(A)):
    ...     for j in range(len(B)):
    ...         for k in range(len(B)):
    ...             C[i][j] += A[i][k] * B[k][j]
    
    >>> C
    [[6, 6], [12, 12], [18, 18]]


"""
