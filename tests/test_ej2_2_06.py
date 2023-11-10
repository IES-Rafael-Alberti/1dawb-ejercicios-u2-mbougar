from src.ej2_2_06 import crear_Triangulo
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, "*\n**\n***\n****\n*****"),
        (1, "*"),
        (2, "*\n**"),
        (10, crear_Triangulo(10))
    ]
)


def test_crear_Triangulo_params(input_n1, expected):
    assert crear_Triangulo(input_n1) == expected

