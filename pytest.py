import pytest
from youtube import *

def add(a,b):
    z = a + b
    return z

def sub(a,b):
    z = a - b
    return z

def mul(a,b):
    z = a * b
    return z

def div(a,b):
    z = a / b
    return z

def div_even(a,b):
    z = a // b
    return z

def modulo(a,b):
    z = a % b
    return z

def sqrt(a):
    if a >= 0:
        z = a ** 0.5
        return z
    return 'negative number'


def test_add_pass():
    assert add(5,5) == 10


def test_add_fail():
    assert add(2,3) == 3


def test_sub_pass():
    assert sub(7,2) == 5


def test_sub_fail():
    assert sub(5,2) == 2


def test_mul_pass():
    assert mul(5,5) == 25


def test_mul_fail():
    assert mul(5,4) == 5


def test_div_pass():
    assert div(10,10) == 1


def test_div_fail():
    with pytest.raises(ZeroDivisionError):
        div(5,0)


def test_div_even_pass():
    assert div_even(5,2) == 2


def test_div_even_fail():
    assert div_even(5,2) == 1


def test_modulo_pass():
    assert modulo(5,4) == 1


def test_modulo_fail():
    assert modulo(5,4) == 2


def test_sqrt_pass():
    assert sqrt(4) == 2


def test_sqrt_pass_negative_number():
    assert sqrt(-2) == 'negative number'