import pytest
from calculator import add, subtract, simple_interest 


def test_add():
    assert add(5,3) == 8
    assert add(10,-13) == -3


def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(-10,-9) == -1


def test_simple_interest(x,y,z):
    assert simple_interest(700,3.4,
                           
       