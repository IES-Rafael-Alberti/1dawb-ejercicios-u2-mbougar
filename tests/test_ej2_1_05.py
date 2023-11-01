from src.ej2_1_05 import comprobar_Edad, comprobar_Ingresos, comprobar_Tributa
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (18, 10, True),
        (5, 10, False),
        (3, 12, False),
        (1, 1, False),
        (17, 16, comprobar_Edad(22, 18))
    ]
)


def test_comprobar_Edad_params(input_n1, input_n2, expected):
    assert comprobar_Edad(input_n1, input_n2) == expected


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1800, 1000, True),
        (500, 1000, False),
        (3000, 3256, False),
        (156, 1200, False),
        (1712, 1645, comprobar_Edad(2200, 1845))
    ]
)


def test_comprobar_Ingresos_params(input_n1, input_n2, expected):
    assert comprobar_Ingresos(input_n1, input_n2) == expected


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (18, 1200, True),
        (5, 1300, False),
        (30, 256, False),
        (15, 120, False),
    ]
)


def test_comprobar_Tributa_params(input_n1, input_n2, expected):
    assert comprobar_Tributa(input_n1, input_n2) == expected
