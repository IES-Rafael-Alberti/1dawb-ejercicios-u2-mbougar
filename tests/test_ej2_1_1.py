from src.ej2_1_1 import repeat_Word
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("Manzana", 2, "Manzana\nManzana"),
        ("10", 10, "10\n10\n10\n10\n10\n10\n10\n10\n10\n10"),
        ("plaTano", 3, "plaTano\nplaTano\nplaTano"),
        ("1", 1, "1"),
        ("PlAtanO", 10, repeat_Word("PlAtanO", 10))
    ]
)


def test_repeat_Word_params(input_n1, input_n2, expected):
    assert repeat_Word(input_n1, input_n2) == expected