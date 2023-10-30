from src.ej2_1_4 import is_Par
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (9, False),
        (0, True),
        (2, True),
        (1, False),
        (7, is_Par(7))
    ]
)


def test_is_Par_params(input_n1, expected):
    assert is_Par(input_n1) == expected