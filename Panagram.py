def panagram(s):
    characters = list("abcdefghijklmnopqrstuvwxyz ")
    for char in characters:
        if char in s:
            continue
        else:
            return False
    return True
s = input("Enter a sentence:")
print(panagram(s))

   

