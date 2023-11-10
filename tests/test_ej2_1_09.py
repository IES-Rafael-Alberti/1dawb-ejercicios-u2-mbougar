from src.ej2_1_09 import asignar_Precio
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (4, 0),
        (10, 5),
        (22, 10),
        (12, 5),
        (74, asignar_Precio(18))
    ]
)


def test_asignar_Precio_params(input_n1, expected):
    assert asignar_Precio(input_n1) == expected
