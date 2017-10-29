"""


[title]: # (Полярные координаты)


Перевод в полярные координаты
=============================

    >>> import math

Используем правило углов арктангенса

    >>> def to_polar(x, y):
    ...     if x == 0 and y == 0:
    ...         return 0.0, 0.0
    ...     r = math.sqrt(x ** 2 + y ** 2)
    ...     phi = 0
    ...     if x > 0:
    ...         if y >= 0:
    ...             phi = math.atan(y / x)
    ...         else:
    ...             phi = math.atan(y / x) + (2 * math.pi)
    ...     elif x < 0:
    ...         phi = math.atan(y / x) + math.pi
    ...     elif x == 0:
    ...         if y > 0:
    ...             phi = math.pi / 2
    ...         elif y < 0:
    ...             phi = 3 * math.pi / 2
    ...     return r, math.degrees(phi)

    # x > 0, y >= 0
    >>> to_polar(x=1, y=0)
    (1.0, 0.0)

    >>> to_polar(x=1, y=1)  # doctest: +ELLIPSIS
    (1.414..., 45.0)

    # x > 0, y < 0
    >>> to_polar(x=1, y=-1)  # doctest: +ELLIPSIS
    (1.414..., 315.0)

    # x < 0
    >>> to_polar(x=-1, y=1)  # doctest: +ELLIPSIS
    (1.414..., 135.0)

    # x = 0, y < 0
    >>> to_polar(x=0, y=-1)  # doctest: +ELLIPSIS
    (1.0, 270.0)

    # x = 0, y = 0
    >>> to_polar(x=0, y=0)  # doctest: +ELLIPSIS
    (0.0, 0.0)

Atan2
-----

Используем функцию atan2 из пакета math

    >>> def to_polar2(x, y):
    ...     r = (x ** 2 + y ** 2) ** (1 / 2)
    ...     phi = math.degrees(math.atan2(y, x))
    ...     return r, phi

    # x > 0, y >= 0
    >>> to_polar2(x=1, y=0)
    (1.0, 0.0)

    >>> to_polar2(x=1, y=1)  # doctest: +ELLIPSIS
    (1.414..., 45.0)

    # x > 0, y < 0
    >>> to_polar2(x=1, y=-1)   # doctest: +ELLIPSIS
    (1.414..., -45.0)

    # x < 0
    >>> to_polar2(x=-1, y=1)   # doctest: +ELLIPSIS
    (1.414..., 135.0)

    # x = 0, y < 0
    >>> to_polar2(x=0, y=-1)
    (1.0, -90.0)

    # x = 0, y = 0
    >>> to_polar2(x=0, y=0)
    (0.0, 0.0)

Polar
-----
    
Используем функцию polar из пакета math 
    
    >>> from cmath import polar

    # x > 0, y >= 0
    >>> polar(complex(1, 0))
    (1.0, 0.0)

    >>> r, phi = polar(complex(1, 1))
    >>> r  # doctest: +ELLIPSIS
    1.414...
    >>> math.radians(45.0)  # doctest: +ELLIPSIS
    0.785...
    >>> phi  # doctest: +ELLIPSIS
    0.785...

    # x > 0, y < 0
    >>> polar(complex(1, -1))  # doctest: +ELLIPSIS
    (1.414..., -0.785...)

    # x < 0
    >>> polar(complex(-1, 1))  # doctest: +ELLIPSIS
    (1.414..., 2.356...)

    # x = 0, y < 0
    >>> polar(complex(0, -1))  # doctest: +ELLIPSIS
    (1.0, -1.570...)

    # x = 0, y = 0
    >>> polar(complex(0, 0))
    (0.0, 0.0)


"""
