from example2 import reverse_string

def test_reverse_basic():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_palindrome():
    assert reverse_string("madam") == "madam"

def test_reverse_with_space():
    assert reverse_string("ab cd") == "dc ba"
