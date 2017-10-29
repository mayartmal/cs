"""


[title]: # (Непрерывный процент)


    >>> import math
    
    
    >>> def get_rate(income):
    ...     if income < 100: return 0.01
    ...     elif income < 1000: return 0.034
    ...     elif income < 5000: return 0.05
    ...     else: return 0.067
    
    
    >>> def percent(p, r, t):
    ...     result = p * math.exp(r * t)
    ...     return result


Подоходный налог
----------------

    >>> get_rate(99)
    0.01
    >>> get_rate(999)
    0.034
    >>> get_rate(4999)
    0.05
    >>> get_rate(5001)
    0.067


Начисление непрерывного процента

    >>> percent(p=100, r=0.1, t=10)
    271.8281828459045
    

"""
