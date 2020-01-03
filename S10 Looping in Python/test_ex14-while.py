import pytest

import random

from unittest.mock import MagicMock

from ex14while import whenIsFive


def test_whenIsFive(monkeypatch):

    # counting by ones, five should be fifth
    monkeypatch.setattr(random, "randint", MagicMock(side_effect = range(1, 10)))
    assert whenIsFive() == 5

    # counting by twos , five should be third
    monkeypatch.setattr(random, "randint", MagicMock(side_effect = range(1, 10, 2)))
    assert whenIsFive() == 3


