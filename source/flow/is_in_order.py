"""


[title]: # (Числа в порядке возрастания)


Числа в порядке возрастания
---------------------------

Напишем функцию, которая проверяет находятся ли числа в порядке возрастания.

    >>> def is_in_order(*args):
    ...     prev = None
    ... 
    ...     for arg in args:
    ...         if prev is not None and arg < prev:
    ...             return False
    ...         prev = arg
    ... 
    ...     return True


    >>> is_in_order(1, 2, 3)
    True

    >>> is_in_order(1, 3, 2)
    False


"""
