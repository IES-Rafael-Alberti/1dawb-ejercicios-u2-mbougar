from src.ej2_1_8 import calcular_Rendimiento , comprobar_Puntuacion
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (1.2, False),
        (0.0, True),
        (0.6, True),
        (1.3, False),
        (0.4, comprobar_Puntuacion(1.0))
    ]
)


def test_comprobar_Puntuacion_params(input_n1, expected):
    assert comprobar_Puntuacion(input_n1) == expected