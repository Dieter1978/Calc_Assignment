import pytest 
from fibonacci import Fibonacci


class Test_Fibonacci:

    def test_fibonacci(self):
        f = Fibonacci()
        assert 34 in f(10)