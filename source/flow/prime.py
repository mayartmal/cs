"""


[title]: # (Множитеи, делители, простые числа)


Множитеи и делители
===================


Поиск делителей
---------------

    >>> def find_primes(n):
    ...     rows = []
    ...     for i in range(1, n + 1):
    ...         row = []
    ...         for j in range(1, n + 1):
    ...             if (i % j) == 0 or (j % i) == 0:
    ...                 row.append(' * ')
    ...             else:
    ...                 row.append('   ')
    ...         rows.append(row)
    ...     return rows


    Если число i делится на j или j делится на i

    >>> for row in find_primes(16):
    ...     print(''.join(row))
     *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
     *  *     *     *     *     *     *     *     * 
     *     *        *        *        *        *    
     *  *     *           *           *           * 
     *           *              *              *    
     *  *  *        *                 *             
     *                 *                    *       
     *  *     *           *                       * 
     *     *                 *                      
     *  *        *              *                   
     *                             *                
     *  *  *  *     *                 *             
     *                                   *          
     *  *              *                    *       
     *     *     *                             *    
     *  *     *           *                       * 


Разложение на множители
-----------------------

    >>> def prime_factors(n):
    ...     factor = 2
    ...     while factor * factor <= n:
    ...         while n % factor == 0:
    ...             n //= factor
    ...             yield factor
    ...         factor += 1
    ...     if n > 1:
    ...         yield n

    >>> list(prime_factors(n=10))
    [2, 5]
    
    >>> list(prime_factors(n=1233))
    [3, 3, 137]


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
