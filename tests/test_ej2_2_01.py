from src.ej2_2_01 import repetir_Palabra
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("hola", 3, "hola hola hola"),
        ("no", 1, "no"),
        ("no", 2, "no no"),
        ("vegetariana", 2, "vegetariana vegetariana"),
        ("vegetariana", 10, repetir_Palabra("vegetariana", 10))
    ]
)


def test_repetir_Palabra_params(input_n1, input_n2, expected):
    assert repetir_Palabra(input_n1, input_n2) == expected
