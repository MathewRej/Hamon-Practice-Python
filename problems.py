# Write a function which takes a single string s as input and which will
#return True if s is a panagram and False if it isn't. 

def panagram(s):
    characters = list("abcdefghijklmnopqrstuvwxyz ")
    for char in characters:
        if char not in s:
            return False
    return True
print("Panagram", panagram("the quick brown fox jumps over the lazy dog"))

# Palindrome - Write a function palindrome which takes one argument s as input and returns True if it's a palindrome. False if not

def palindrome(s):
    word = ""
    for letter in s:
        word = letter + word
    if word == s:
        return True
    else:
        return False
print("Palindrome", palindrome("madam"))

# Primality - Write a function prime which will take a number n as input and return True if n is a prime number and False otherwise

def prime(n):
    if(n > 1):
        for i in range(2, n):
            if(n % i == 0):
                return False
            else:
                return True
    else:
        return False
print("Prime", prime(0))

# Frequency - Write a function called freq which will take a string s as input and return a dictionary of frequencies of each letter in s 

def freq(s):
    words = {}
    for char in s:
        if char not in words:
            words[char] = 1
        else:
            words[char] += 1
    return words
print("Frequency", freq("helllllo"))
            