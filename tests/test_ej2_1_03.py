from src.ej2_1_03 import division
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (10, 2, "5.0"),
        (5, 0, "Error"),
        (3, 2, "1.5"),
        (1, 1, "1.0"),
        (7, 7, division(7, 7))
    ]
)


def test_division_params(input_n1, input_n2, expected):
    assert division(input_n1, input_n2) == expected
