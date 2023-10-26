from src.ej2_1_2 import check_Password_Attempt
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("contraseña", "contraseña", True),
        ("CONTRASEÑA", "contraseña", True),
        ("hbscnjUHCDnjcj", "contraseña", False),
        ("1", "1", True),
        ("contraseña", "CONTRASEÑA", True),
        ("PlAtanO", "platano", check_Password_Attempt("contraseña", "contraseña"))
    ]
)


def test_check_Password_Attempt_params(input_n1, input_n2, expected):
    assert check_Password_Attempt(input_n1, input_n2) == expected