def panagram(s):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    for char in characters:
        if char not in s:
            return False
    return True
print(panagram("the quick brown fox jumps over the lazy dog"))

   

