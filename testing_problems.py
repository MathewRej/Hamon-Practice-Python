
from problems import freq, palindrome, prime, panagram

# Testing Palindrome
def test_palindrome():
    assert palindrome("madam"), True
    assert not palindrome("mathew"), False

# Testing Panagram
def test_panagram():
    assert panagram("the quick brown fox jumps over the lazy dog"), True
    assert panagram("abcdefghijklmnopqrstuvwxyz"), True
    assert not panagram("my name is mathew"), False

# Testing prime

def test_prime():
    assert prime(41), True
    assert not prime(1), False
    assert not prime(0), False

#Testing Frequency
def test_freq():
    s = "hellloo"
    test_freq = {'h': 1, 'e': 1, 'l': 3, 'o': 2}
    assert freq(s) == test_freq