"""


[title]: # (Коллекция купонов)


Коллекция купонов
=================

    >>> import random 

    >>> n = 10**3

    >>> isCollected = [False for _ in range(n)]
    >>> collected = 0
    >>> count = 0

    >>> while collected < n:
    ...     value = random.randrange(n)
    ...     count += 1
    ...     if not isCollected[value]:
    ...         collected += 1
    ...         isCollected[value] = True

    >>> print(count)


"""
