"""


[title]: # (Квадратное уравнение)



Квадратное уравнение
====================


    >>> import math
    
    >>> def quadratic(a, b, c):
    ...     D = (b * b) - (4 * a * c)
    ...     d = math.sqrt(D)
    ...     x1 = (-b - d) / 2 * a
    ...     x2 = ( b - d) / 2 * a
    ...     return x1, x2


    >>> x1, x2 = quadratic(1, 2, 1)
    >>> x1
    -1.0
    >>> x2
    1.0


"""
