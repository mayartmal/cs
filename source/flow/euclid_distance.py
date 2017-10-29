"""


[title]: # (Евклидово расстояние)


Евклидово расстояние между двумя точками
----------------------------------------

    >>> import math
    >>> z = math.sqrt(2)
    >>> z  # doctest: +ELLIPSIS
    1.41...

    >>> def euclid_distance(p1, p2):
    ...     return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    >>> from collections import namedtuple
    >>> Point = namedtuple('Point', 'x y')
    
    >>> p1 = Point(1, 1)
    >>> p2 = Point(2, 2)
    >>> d = euclid_distance(p1, p2)
    >>> d  # doctest: +ELLIPSIS
    1.41...
    

"""
