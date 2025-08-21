from example1 import is_even

# Positive even numbers
def test_even_positive():
    assert is_even(2) is True
    assert is_even(10) is True

# Positive odd numbers
def test_odd_positive():
    assert is_even(3) is False
    assert is_even(17) is False

# Zero (special case - even number)
def test_zero_is_even():
    assert is_even(0) is True

# Negative numbers
def test_negative_numbers():
    assert is_even(-2) is True
    assert is_even(-7) is False
