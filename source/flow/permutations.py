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



Случайные перестановки
======================

Выборка неповторяющихся элементов.

    >>> import random

    >>> def sample(a, n):
    ...     res = []
    ...     s = a
    ...     for i in range(n):
    ...         r = random.randrange(i, n)
    ...         res.append(s[r])
    ...         s[r], s[i] = s[i], s[r]
    ...     return res

    >>> random.seed(5)
    >>> a = [3, 4, 1, 2, 5]
    >>> sample(a, 5)
    [5, 2, 3, 1, 4]

    >>> sample(a, 2)
    [2, 5]


Встроенная функция sample

    >>> random.seed(5)
    >>> a = [3, 4, 1, 2, 5]
    >>> random.sample(a, 5)
    [5, 1, 2, 4, 3]


"""
