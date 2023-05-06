import pytest
from calculator import add, subtract, simple_interest, fibonacci_of, multiply, divide, square, cube, compound_interest


def test_add():
    assert add(5,3) == 8
    assert add(10,-13) == -3

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(-10,-9) == -1

def test_multiply():
    assert multiply(57,78) == 4446

def test_divide():
    assert divide(789,4) == 197.25

def test_square():
    assert square(568) == 322624

def test_cube():
    assert cube(9) == 729

def test_simple_interest():
    assert simple_interest(700,3.4,5) == 119

def test_compound_interest():
    assert compound_interest(1500,5.8,10) == 2636.015356929926

                           
def test_fibonacci_of():
    assert 34 in fibonacci_of(10)
