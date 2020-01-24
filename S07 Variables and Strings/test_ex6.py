import pytest

from ex6 import greet_name


def test_greeting():
    assert greet_name == "foo Heisenberg"

