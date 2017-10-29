"""


[title]: # (Парсим аргументы)


Парсим аргументы
================

Пример использования парсера аргументов командной строки

    >>> import argparse

    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('-a', action='store')
    >>> args = parser.parse_args()

    >>> if args.a == 'build':
    ...     pass
    ... elif args.a == 'clear':
    ...     pass


"""
