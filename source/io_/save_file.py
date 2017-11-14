"""


[title]: # (Пишем и читаем файл)


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


Пишем и читаем файл ключ-значение
=================================
Записывает и считывает простой файл.

    file sep.txt
    ------------
    a 1
    b 2

    >>> x = [
    ...     ('a', 1),
    ...     ('b', 2)
    ... ]

    # Пишем
    >>> with open('sep.txt', 'w') as f:
    ...     for key, value in x:
    ...         _ = f.write("{} {}\\n".format(key, value))

    # Читаем
    >>> with open('sep.txt', 'r') as f:
    ...     for line in f:
    ...         print(line.split())
    ['a', '1']
    ['b', '2']


"""
