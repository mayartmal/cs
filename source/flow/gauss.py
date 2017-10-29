"""


[title]: # (Гауссовы случайные числа)


Гауссовы случайные числа
------------------------

    >>> import math
    >>> import random
    
    
    >>> def gauss(count: int):
    ...     for _ in range(count):
    ...         v = random.random()
    ...         u = random.random()
    ...         z = math.sin(2 * math.pi * v) * (-2 * math.log(u)) ** (1 / 2)
    ...         yield z
    
    >>> random.seed(2)
    >>> count = 9
    >>> for x in gauss(count):
    ...    print(round(x, 2))
    -0.09
    0.77
    -0.67
    -1.34
    -0.62
    -0.94
    0.58
    -0.1
    -0.34


"""
