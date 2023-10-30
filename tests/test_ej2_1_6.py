from src.ej2_1_6 import comprobar_Nombre, comprobar_Sexo
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("Manuel", 12),
        ("paula", 16),
        ("Rodrigo", 18),
        ("bonifacio", 1),
        ("Ana", comprobar_Nombre("alejandro"))
    ]
)


def test_comprobar_Nombre_params(input_n1, expected):
    assert comprobar_Nombre(input_n1) == expected


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("test", "Error"),
        ("masculino", "masculino"),
        ("Femenino", "femenino"),
        ("Manuel", "Error"),
        ("Femenino", comprobar_Sexo("femenino"))
    ]
)


def test_comprobar_Sexo_params(input_n1, expected):
    assert comprobar_Sexo(input_n1) == expected