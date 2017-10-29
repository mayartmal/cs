"""


[title]: # (Метод Монте-Карло)


Метод Монте-Карло
=================

    >>> import random
    >>> random.seed(2)

    >>> bets = 0
    >>> wins = 0
    >>> trials = 1000
    >>> stake = 10
    >>> goal = 20

    >>> for t in range(trials):
    ...     cash = stake
    ...     while 0 < cash < goal:
    ...         bets += 1
    ...         if random.randrange(0, 2) == 0:
    ...             cash += 1
    ...         else:
    ...             cash -= 1
    ...     if cash == goal:
    ...         wins += 1

    >>> print('p = ' + str(100 * wins // trials) + '% wins')
    p = 46% wins
    >>> print('Ср. к-во ставок в одной попытке: ' + str(bets // trials))
    Ср. к-во ставок в одной попытке: 101


"""
