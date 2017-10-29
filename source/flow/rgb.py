"""


[title]:  #  (RGB и CMYK)


RGB и CMYK
==========


Приведение цвета к печатному типу
---------------------------------

    >>> from collections import namedtuple
    
    
    >>> RGB = namedtuple('RGB', 'r g b')
    >>> CMYK = namedtuple('CMYK', 'c m y k')
    
    
    >>> def get_cmyk(rgb: RGB):
    ...     if not all(rgb):
    ...         return CMYK(0, 0, 0, k=1)
    ...     r, g, b = rgb
    ...     w = max(r / 255, g / 255, b / 255)
    ...     c = (w - r / 255) / w
    ...     m = (w - g / 255) / w
    ...     y = (w - b / 255) / w
    ...     k = 1 - w
    ...     return CMYK(c, m, y, k)


    >>> color = RGB(0, 0, 0)
    >>> get_cmyk(color)
    CMYK(c=0, m=0, y=0, k=1)

    >>> color = RGB(120, 60, 100)
    >>> get_cmyk(color)
    CMYK(c=0.0, m=0.5, y=0.16666666666666666, k=0.5294117647058824)


"""
