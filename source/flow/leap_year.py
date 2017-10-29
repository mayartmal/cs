"""


[title]: # (Високосный год)


Високосный год
==============

    >>> def leapyear(y):
    ...     return all([
    ...         y % 4 == 0,
    ...         y % 100 != 0,
    ...         y % 400 != 0
    ...     ])


    >>> leapyear(2016)
    True
    
    >>> leapyear(2017)
    False

    
"""
