"""


[title]: # (Расстояния)


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


Большая окружность
------------------

На вход принимает широту и долготу в градусах.
На выходе большая окружность в навигационных милях.

Расстояние между Парижем, Франция и Сан-Франциско, штат Калифорния, США
8964 км = 5570 миль

    >>> from math import acos, sin, cos, radians, log
    
    >>> def big_circle(x1, y1, x2, y2):
    ...     rx1 = radians(x1)
    ...     rx2 = radians(x2)
    ...     ry = radians(y1 - y2)
    ...     ang = sin(rx1) * sin(rx2) + cos(rx1) * cos(rx2) * cos(ry)
    ...     result = 60 * acos(ang)
    ...     return result
    
    
    >>> def mercator(phi, lam, lam0):
    ...     num = 1 + sin(phi)
    ...     den = 1 - sin(phi)
    ...     x = lam - lam0
    ...     y = 1 / 2 * log(1 + sin(num / den))
    ...     return x, y


    >>> paris = (48.87, -2.33)
    >>> san_francisco = (37.8, 122.4)
    >>> big_circle(*paris, *san_francisco)
    84.26870278998847

Проекция Меркатора
    
    >>> phi = 12
    >>> lam = 10
    >>> lam0 = 1
    >>> mercator(phi, lam, lam0)
    (9, 0.13004480476579486)


"""
