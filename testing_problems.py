import pytest
from problems import freq, palindrome, prime, panagram

# Testing Palindrome
def test_palindrome():
    assert(palindrome("madam"), True)
    assert(palindrome("mathew"), False)

# Testing Panagram
def test_panagram():
    assert(panagram("the quick brown fox jumps over the lazy dog"), True)
    assert(panagram("abcdefghijklmnopqrstuvwxyz"), True)
    assert(panagram("my name is mathew"), False)

# Testing prime

def test_prime():
    assert(prime(41), True)
    assert(prime(1), False)
    assert(prime(0), False)

#Testing Frequency
def test_freq():
    assert(freq("hellloo"), {'h': 1, 'e': 1, 'l': 3, 'o': 2})
    assert(freq("mathew"), {'m':1, 'a':1, 't':1, 'h':1, 'e':1, 'w':1})