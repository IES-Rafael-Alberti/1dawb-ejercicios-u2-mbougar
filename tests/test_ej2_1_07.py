from src.ej2_1_07 import comprobar_Renta
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (32000, 20),
        (500000, 45),
        (58003, 30),
        (18654, 15),
        (7000, comprobar_Renta(5))
    ]
)


def test_comprobar_Renta_params(input_n1, expected):
    assert comprobar_Renta(input_n1) == expected
