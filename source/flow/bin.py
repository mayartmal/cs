"""


[title]: # (Двоичная форма)


Двоичная форма
==============

    >>> def pow2(n):
    ...     if n < 0:
    ...         raise ValueError('need n >= 0')
    ...     power = 1
    ...     i = 0
    ...     while i <= n:
    ...         yield power
    ...         power *= 2
    ...         i += 1
    
    
    >>> def close2power(n):
    ...     power = 1
    ...     while 2 * power <= n:
    ...         power *= 2
    ...     return power
    
    
    >>> def to_b(n):
    ...     result = []
    ... 
    ...     v = 1
    ...     while v <= n // 2:
    ...         v *= 2
    ... 
    ...     while v > 0:
    ...         if n < v:
    ...             result.append('0')
    ...         else:
    ...             result.append('1')
    ...             n -= v
    ...         v //= 2
    ... 
    ...     return ''.join(result)
    
    
    >>> def to_i(n):
    ...     result = sum(pow(2, i) for i, x in enumerate(reversed(n)) if x == '1')
    ...     return result


Таблица степеней двойки
-----------------------

    >>> n = -1
    >>> for i, x in enumerate(pow2(n)): # doctest: +ELLIPSIS
    ...     i, x
    Traceback (most recent call last):
      ...
    ValueError: need n >= 0

    >>> n = 10
    >>> for i, x in enumerate(pow2(n)):
    ...     i, x
    (0, 1)
    (1, 2)
    (2, 4)
    (3, 8)
    (4, 16)
    (5, 32)
    (6, 64)
    (7, 128)
    (8, 256)
    (9, 512)
    (10, 1024)
    
    >>> list(x for x in pow2(10))
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]


Целое степени двойки ближайшее к заданному целому
-------------------------------------------------

    >>> close2power(3)
    2
    
    >>> close2power(10)
    8


Перевод числа в двоичную форму
------------------------------

    >>> n = 19
    >>> to_b(n)
    '10011'
    
Встроенная функция

    >>> bin(n)
    '0b10011'


Перевод двоичного числа в целое

    >>> to_i('10011')
    19


"""
