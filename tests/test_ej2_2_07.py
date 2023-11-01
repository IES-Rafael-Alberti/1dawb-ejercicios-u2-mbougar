from src.ej2_2_07 import crear_Tabla
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, "1 x 10 = 10\n2 x 10 = 20\n3 x 10 = 30\n4 x 10 = 40\n5 x 10 = 50"),
        (1, "1 x 10 = 10"),
        (2, "1 x 10 = 10\n2 x 10 = 20"),
        (10, crear_Tabla(10))
    ]
)


def test_crear_Tabla_params(input_n1, expected):
    assert crear_Tabla(input_n1) == expected

