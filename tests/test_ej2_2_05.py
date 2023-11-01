from src.ej2_2_05 import calcular_Capital
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (500, 10, 550),
        (1000, 50, 1500),
        (2653, 30, 3448.9),
        (20000, 100, 40000),
        (10000, 20 , calcular_Capital(10000, 20))
    ]
)


def test_calcular_Capital_params(input_n1, input_n2, expected):
    assert calcular_Capital(input_n1, input_n2) == expected

