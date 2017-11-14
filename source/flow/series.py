"""


[title]: # (Ряды и суммы)


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

Ряды
====

    >>> def odd_sign_ones(n):
    ...     result = 0
    ...     for i in range(1, n+1):
    ...         sign = -1 if i % 2 == 0 else 1
    ...         result += sign * 1
    ...     return result


    >>> def x_powers(x, n):
    ...     result = 0
    ...     temp = 1
    ...     for i in range(1, n+1):
    ...         temp *= x
    ...         result += temp
    ...     return result
    
    
    >>> def odd_sign_x_powers(x, n):
    ...     result = 0
    ...     temp = 1
    ...     for i in range(1, n+1):
    ...         temp *= x
    ...         sign = -1 if i % 2 == 0 else 1
    ...         result += sign * temp
    ...     return result
    
    
    >>> def odd_powers_x(x, n):
    ...     result = 0
    ...     temp = 1
    ...     for i in range(1, n+1):
    ...         temp *= x
    ...         if i % 2 != 0:
    ...             result += temp
    ...     return result
    
    
    >>> def odd_sign_powers_x(x, n):
    ...     result = 0
    ...     temp = 1
    ...     z = 1
    ...     for i in range(1, n+1):
    ...         temp *= x
    ...         if i % 2 != 0:
    ...             sign = -1 if z % 2 == 0 else 1
    ...             result += sign * temp
    ...             z += 1
    ...     return result
    
    
    >>> def factseq(n):
    ...     result = 0
    ...     temp = 1
    ...     for i in range(1, n + 1):
    ...         temp *= i
    ...         result += temp
    ...     return result
    
    
    >>> def taylor(x, n):
    ...     result = 1
    ...     temp = 1
    ...     for i in range(1, n + 1):
    ...         temp *= x / i
    ...         result += temp
    ...     return result
    
    
    >>> def sine(x, n):
    ...     result = 0
    ...     temp = 1
    ...     z = 1
    ...     for i in range(1, n+1):
    ...         temp *= x / i
    ...         if i % 2 != 0:
    ...             sign = -1 if z % 2 == 0 else 1
    ...             result += sign * temp
    ...             z += 1
    ...     return result
    
    
    >>> def cosine(x, n):
    ...     result = 1
    ...     temp = 1
    ...     z = 1
    ...     for i in range(1, n+1):
    ...         temp *= x / i
    ...         if i % 2 == 0:
    ...             sign = -1 if z % 2 != 0 else 1
    ...             result += sign * temp
    ...             z += 1
    ...     return result



Последовательность чередующихся единиц

    >>> 1 - 1 + 1 - 1 + 1
    1
    >>> odd_sign_ones(5)
    1


Степенной ряд

    >>> x = 2
    >>> z = x + x**2 + x**3 + x**4 + x**5
    >>> z
    62
    >>> x_powers(x=2, n=5)
    62


Чередующийся степенной ряд
    
    >>> x = 2
    >>> z = x - x**2 + x**3 - x**4 + x**5
    >>> z
    22
    >>> odd_sign_x_powers(x=2, n=5)
    22


Нечетный степенной ряд

    >>> x = 2
    >>> z = x + x**3 + x**5 + x**7
    >>> z
    170
    >>> odd_powers_x(x=2, n=7)
    170


Чередующийся нечетный степенной ряд
    
    >>> x = 2
    >>> z = x - x**3 + x**5 - x**7
    >>> z
    -102
    >>> odd_sign_powers_x(x=2, n=7)
    -102


Ряд факториалов

    >>> 1 + 1*2 + 1*2*3 + 1*2*3*4
    33
    >>> factseq(4)
    33


Taylor series

    >>> x = 2
    >>> 1 + x/1 + x**2 / (1*2) + x**3 / (1*2*3)
    6.333333333333333
    >>> taylor(x=2, n=3)
    6.333333333333333


Синус

    >>> x = 2
    >>> x - x**3 / (1*2*3) + x**5 / (1*2*3*4*5)
    0.9333333333333333
    >>> sine(x=2, n=5)
    0.9333333333333333


Косинус

    >>> x = 2
    >>> 1 - x**2/(1*2) + x**4/(1*2*3*4)
    -0.33333333333333337
    
    >>> cosine(x=2, n=4)
    -0.33333333333333337

"""
