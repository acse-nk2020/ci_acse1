from functools import lru_cache

__all__ = ['my_sum', 'factorial', 'my_product']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache()
def factorial(n):
    return n * factorial(n - 1) if n else 1


def my_product(iterable):
    tot = 1
    for i in iterable:
        tot = tot * i
    return tot
