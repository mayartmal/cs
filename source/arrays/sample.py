"""


[title]: # (Случайные перестановки)


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
