"""


[title]: # (Перестановки)


Перестановки
============

    >>> import random
    >>> from itertools import product, permutations

    >>> random.seed(2)

    >>> x = [0, 1]

    Product:
    >>> for p in product(x, repeat=2):
    ...     print(p)
    (0, 0)
    (0, 1)
    (1, 0)
    (1, 1)


    Shuffle:
    >>> for _ in range(2):
    ...     random.shuffle(x)
    ...     print(x)
    [1, 0]
    [0, 1]

    Permutations:
    >>> for p in permutations(x):
    ...     print(p)
    (0, 1)
    (1, 0)

    Manual:
    >>> z = [0, 1]
    >>> n = 2
    >>> for i in range(n):
    ...     r = random.randrange(i, n)
    ...     z[r], z[i] = z[i], z[r]
    >>> print(z)
    [0, 1]


"""
