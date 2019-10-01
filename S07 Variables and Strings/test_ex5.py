import pytest

from ex5 import message, mountains, quotation

def test_escape_sequences():
    assert message == '''foo
bar'''
    assert mountains == '/\\/\\/\\'
    assert quotation == '"biteme"'
