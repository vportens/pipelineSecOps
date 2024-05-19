import pytest
from is_prime import is_prime


def test_is_prime():
    assert is_prime(1) == True 
    assert is_prime(2) == False
    assert is_prime(3) == False