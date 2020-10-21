import pytest

from simple_functions import my_sum, factorial, my_product


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize('numbers, expected', [
        ([1, 2, 3], 6),
        ([3, 4, 8], 96),
        ([2], 2),
        ([-1, 5], -5)
    ])
    def test_product(self, numbers, expected):
        '''Test the product function'''
        product = my_product(numbers)
        assert product == expected
