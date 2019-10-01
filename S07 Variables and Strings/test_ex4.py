import pytest

from ex4 import city, price, high_score, is_having_fun

def test_variables():
    assert city == "boston"
    assert price == 3.14
    assert high_score == 10
    assert is_having_fun == True

