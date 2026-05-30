import pytest

from fuel_2 import convert, gauge
#from fuel_2 import gauge

def test_fuel_2_convert_Normal():
    assert convert("2/4") == float(2/4)
    assert convert("0/4") == float(0/4)
    assert convert("4/4") == float(4/4)

def test_fuel_2_convert_ValueError():
    with pytest.raises(ValueError):
        convert("-3/4")
        convert("4/-3")

def test_fuel_2_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(float(0/100)) == "E"
    assert gauge(float(1/100)) == "E"
    assert gauge(float(99/100)) == "F"
    assert gauge(float(100/100)) == "F"
    assert gauge(float(1/4)) == "25%"
    assert gauge(float(3/4)) == "75%"
 

