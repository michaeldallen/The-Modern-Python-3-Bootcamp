import pytest
from unittest.mock import MagicMock

from ex10 import find_food_group


food_group_test_data = [
    ("apple", "fruit"),
    ("steak", "meat"), 
    ("dirt",  ""),
]



@pytest.mark.parametrize("food,food_group", food_group_test_data)
def test_oddity(food, food_group, monkeypatch):
    print(f"food: {food}, expected food group: {food_group}")
    mock_print = MagicMock()
    monkeypatch.setattr("builtins.print", mock_print)
    find_food_group(food)
    mock_print.assert_called_once_with(food_group)
                         
