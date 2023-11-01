from src.ej2_2_10 import comprobar_Primo
import pytest


@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (5, True),
        (1645, False),
        (743, True),
        (661, comprobar_Primo(2))
    ]
)


def test_comprobar_Primo_params(input_n1, expected):
    assert comprobar_Primo(input_n1) == expected

