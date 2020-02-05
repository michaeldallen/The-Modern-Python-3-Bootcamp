import pytest

from ex16_lists import thisForThat


def test_thisForThat():
    assert thisForThat(["Hanna"]) == ["Hannah"]
    assert thisForThat(["Geoffrey"]) == ["Jeffrey"]
    assert thisForThat(["aparna"]) == ["Aparna"]
    assert thisForThat(["foo"]) == ["foo"]
    assert thisForThat(["bar"]) == ["bar"]
    assert thisForThat(["foo", "bar"]) == ["foo", "bar"]

    raw = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]
    cooked = ["Hannah", "Louisa", "Claudia", "Angela", "Jeffrey", "Aparna"]
    assert thisForThat(raw) == cooked





