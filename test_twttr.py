import pytest

from twttr import shorten

def test_shorten():
    assert shorten("choi") == "ch"
    assert shorten("234") == "234"
    assert shorten("CHOI Sanghoon") == "CH Snghn"




