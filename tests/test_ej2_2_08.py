from src.ej2_2_08 import crear_Triangulo
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, "1\n3 1\n5 3 1"),
        (1, "1"),
        (2, "1"),
        (10, crear_Triangulo(10))
    ]
)


def test_crear_Triangulo_params(input_n1, expected):
    assert crear_Triangulo(input_n1) == expected

