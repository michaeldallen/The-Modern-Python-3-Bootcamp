import pytest

from ex13ranges import oddFromTenToTwentyInclusive, sumOfList


def test_oddFromTenToTwentyInclusive():
    assert oddFromTenToTwentyInclusive() == [11, 13, 15, 17, 19]

def test_sumOfList():
    assert sumOfList([1,2,3]) == 62
    assert sumOfList([11,22,33]) == 66

    

    

    
    

