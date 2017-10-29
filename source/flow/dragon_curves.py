"""


[title]: # (Кривые дракона)


Кривые дракона
==============

    >>> def inv_mid(text):
    ...     if len(text) % 2 == 0:
    ...         raise ValueError('text must be odd')
    ...     mid = len(text) // 2
    ...     list_ = list(text)
    ...     list_[mid] = '0' if text[mid] == '1' else '1'
    ...     return ''.join(list_)
    
    
    >>> def gen_dragon(n):
    ...     d = '1'
    ...     for x in range(n):
    ...         yield d
    ...         d = d + '1' + inv_mid(d)


    >>> inv_mid('10') # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: text must be odd
    
    >>> inv_mid('101')
    '111'

    >>> inv_mid('010')
    '000'
    
    >>> n = 4
    >>> for x in gen_dragon(n):
    ...     x
    '1'
    '110'
    '1101100'
    '110110011100100'


"""
