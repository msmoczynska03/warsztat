import pytest

def f1(a):
    return a ** 2
def test():
    assert f1(5) == 25
