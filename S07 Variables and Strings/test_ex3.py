import pytest

from ex3 import divideByFive


def test_divideCashByFive():
    initial_cash = 19867324678987.99
    one_fifth_cash = 3973464935797.5977
    assert divideByFive(initial_cash) == one_fifth_cash
