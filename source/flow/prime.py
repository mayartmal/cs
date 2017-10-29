"""


[title]: # (Множитеи и делители)


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


"""
