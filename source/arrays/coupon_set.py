"""


[title]: # (Коллекция купонов. Множество)


Коллекция купонов. Множество
============================


    >>> import random
    
    >>> n = 10**3

    >>> isCollected = set()
    >>> collected = 0
    >>> count = 0

    >>> while collected < n:
    ...     value = random.randrange(n)
    ...     count += 1
    ...     if value in isCollected:
    ...         continue
    ...     collected += 1
    ...     isCollected.add(value)

    >>> print(count)
    
    
"""
