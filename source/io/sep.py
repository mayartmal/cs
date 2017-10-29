""""


[title]: # (Пишем и читаем файл)


Пишем и читаем файл
===================


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
