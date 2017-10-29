"""


[title]: # (Пишем и читаем json файл)


Пишем и читаем json файл
========================
    
    >>> import json
    
    >>> x = {
    ...     'a': 1,
    ...     'b': 2
    ... }
    
    
    # Пишем
    >>> with open('x.json', 'w') as f:
    ...     _ = f.write(json.dumps(x))
    
    
    # Читаем
    >>> with open('x.json', 'r') as f:
    ...     z = json.load(f)
    
    
    >>> print(isinstance(z, dict))
    True
    >>> print(z['a'])
    1


"""
