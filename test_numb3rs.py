import pytest
from numb3rs import validate

def test_validate():
    assert validate("1.2.4.5") == True
    assert validate("1.2.4") == False
    assert validate("1.4.2.34.23") == False
    assert validate("1.asdf.4.5") == False
    assert validate("1.0.4.255") == True
    assert validate("0.2.4.256") == False

@pytest.mark.parametrize("input, result", [
    ("1.2.4.5", True),
    ("1.2.4", False),
    ("1.2.4.34.5", False),
    ("1.2.asdf.5", False),
    ("1.0.4.255", True),
    ("1.0.4.256", False),
])

def test_validate2(input, result):
    assert validate(input) == result
