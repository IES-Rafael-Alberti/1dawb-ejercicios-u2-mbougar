from src.ej2_2_02 import calcular_Años
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, "1-2-3-4-5."),
        (1, "1."),
        (2, "1-2."),
        (20, "1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20."),
        (10, calcular_Años(10))
    ]
)


def test_calcular_Años_params(input_n1, expected):
    assert calcular_Años(input_n1) == expected
