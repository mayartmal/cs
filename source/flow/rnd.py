"""


[title]:  #  (Случайные числа)


Случайные числа
===============

    >>> import random
    >>> import reprlib
    >>> from collections import namedtuple

    Генерирует один случайный бросок монетки
    >>> def flip():
    ...     return 'Орел' if random.randrange(0, 2) == 0 else 'Решка'

    Генерирует бросок игральной кости
    >>> def roll():
    ...     return random.randrange(1, 7)

    >>> RndResults = namedtuple('RndResults', 'list max min mid')

    >>> def rng(n):
    ...     rs = list(random.random() for _ in range(n))
    ...     mn = min(rs)
    ...     mx = max(rs)
    ...     md = sum(rs) / len(rs)
    ...     return RndResults(rs, mn, mx, md)

    >>> random.seed(10)

    Случайные броски монетки
    >>> list(flip() for _ in range(3))
    ['Орел', 'Решка', 'Решка']

    Случайные броски кубика
    >>> list(roll() for _ in range(3))
    [5, 1, 2]

    Равномерные случайные числа
    >>> r = rng(10)
    >>> reprlib.repr(r.list)  # doctest: +ELLIPSIS
    '[0.462..., 0.491..., 0.277..., 0.810..., 0.0344..., 0.490..., ...]'
    >>> 'Минимум: {:.2f}, Максимум: {:.2f}, Среднее: {:.2f}'.format(*r[1:])
    'Минимум: 0.03, Максимум: 0.95, Среднее: 0.47'


"""
