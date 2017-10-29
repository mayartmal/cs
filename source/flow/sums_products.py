"""


[title]: # (Суммы)


Суммы
=====

Сумма ряда чисел
----------------
    
    >>> 1 + 2 + 3 + 4 + 5
    15
    
    \sum_{i=0}^{n-1} total_{i}
    
    >>> k = 5
    >>> total = 0.0
    >>> for i in range(1, k + 1):
    ...     total += i
    >>> total
    15.0

    >>> a = [1, 2, 3, 4, 5]
    >>> sum(a)
    15

    \sum_{i=1}^{k}n =  \frac{k \cdot (k+1)}{2}
    
    >>> k = 5 
    >>> (k * (k + 1)) / 2
    15.0


Произведение ряда чисел (Факториал)
-----------------------------------

    \prod_{i=1}^{k}i = 1 \cdot 2 \cdot 3 \cdot 4 \cdot ...
    
    >>> 1 * 2 * 3 * 4 * 5
    120
    
    >>> n = 5
    >>> product = 1.0
    >>> for i in range(1, n + 1):
    ...     product *= i
    >>> product
    120.0

Приближенное значение по формуле Стирлинга

    \sqrt{2\cdot \pi n}\cdot \left ( \frac{n}{e} \right )^{n}

    >>> import math
    >>> n = 5
    >>> f = math.sqrt(2 * math.pi * n) * math.pow(n / math.e, n)
    >>> f  # doctest: +ELLIPSIS
    118.0191679575901


"""
