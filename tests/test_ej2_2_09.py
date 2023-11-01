from src.ej2_2_09 import comprobar_Contraseña
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("hola", "contraseña", False),
        ("Contraseña", "contraseña", False),
        ("contraseña", "contraseña",  True),
        ("hola", "hola", comprobar_Contraseña("contraseña", "contraseña"))
    ]
)


def test_comprobar_Contraseña_params(input_n1, input_n2, expected):
    assert comprobar_Contraseña(input_n1, input_n2) == expected

