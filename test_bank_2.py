import pytest
from bank_2 import value

def test_value():
    assert value("hello, there") == "$0"
    assert value("hi") == "$20"
    assert value("Good Morning") == "$100"
    assert value("say hello") == "$100"