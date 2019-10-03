import pytest

from ex12 import am_i_calling_in_sick


sickiness_scenarios = [
    (True,  True,  True,  True,  True),
    (True,  True,  True, False, False),
    (True,  True, False,  True,  True),
    (True,  True, False, False, False),

    (True, False,  True,  True,  True),
    (True, False,  True, False, False),
    (True, False, False,  True,  True),
    (True, False, False, False, False),

    (False,  True,  True,  True,  True),
    (False,  True,  True, False, False),
    (False,  True, False,  True, False),
    (False,  True, False, False, False),

    (False, False,  True,  True, False),
    (False, False,  True, False, False),
    (False, False, False,  True, False),
    (False, False, False, False, False),

    
]


@pytest.mark.parametrize("actually_sick,kinda_sick,hate_your_job,sick_days,call_in_sick", sickiness_scenarios)
def test_calling_in_sick(actually_sick, kinda_sick, hate_your_job, sick_days, call_in_sick):
    assert am_i_calling_in_sick(actually_sick, kinda_sick, hate_your_job, sick_days) == call_in_sick
