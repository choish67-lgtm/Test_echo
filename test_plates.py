import pytest

from plates import is_valid_2

def test_is_valid_2():
    assert is_valid_2("abc123") == True
    assert is_valid_2("ab") == True
    assert is_valid_2("ab490") == True
    assert is_valid_2("abcdef") == True
    assert is_valid_2("ab023") == False
    assert is_valid_2("ab23a") == False
    assert is_valid_2("abcde23") == False
    assert is_valid_2("23") == False
    assert is_valid_2("c") == False
    assert is_valid_2("c d") == False