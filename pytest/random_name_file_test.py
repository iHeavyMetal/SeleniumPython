import pytest

def test_random():
    x=5
    y=2
    assert x+y==5, "Assertion failed. Expected 5 but was " + str(x+y)
    assert x+y==7, "Assertion failed. Expected 7"

