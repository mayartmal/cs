"""


[title]: # (Решето Эратосфена)


Решето Эратосфена
=================

    >>> def sieve(n):
    ...     is_prime = [True for _ in range(n + 1)]
    ... 
    ...     for i in range(2, n):
    ...         if is_prime[i]:
    ...             for j in range(2, n//i + 1):
    ...                 is_prime[i*j] = False
    ... 
    ...     return sum(is_prime[i] for i in range(2, n))

Рассчитывает количество простых множителей <= n

    >>> sieve(25)
    9

    >>> sieve(100)
    25
    
    >>> sieve(10000)
    1229


"""
