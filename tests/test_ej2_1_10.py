from src.ej2_1_10 import comprobar_Ingrediente, comprobar_Tipo
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("no vegetariana", 3, "salmón"),
        ("no vegetariana", 1, "peperoni"),
        ("no vegetariana", 2, "jamón"),
        ("vegetariana", 2, "tofu"),
        ("vegetariana", 1, comprobar_Ingrediente("vegetariana", 1))
    ]
)


def test_comprobar_Ingrediente_params(input_n1, input_n2, expected):
    assert comprobar_Ingrediente(input_n1, input_n2) == expected


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("No vegetariana", True),
        ("hola", False),
        ("no  vegetariana", False),
        ("vegetariana", True),
        ("no vegetariana", comprobar_Tipo("vegetariana"))
    ]
)


def test_comprobar_Tipo_params(input_n1, expected):
    assert comprobar_Tipo(input_n1) == expected