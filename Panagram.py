def panagram():
    s = input("Enter a sentence:")
    characters = list("abcdefghijklmnopqrstuvwxyz ")
    for char in characters:
        if char in s:
            continue
        else:
            return False
    return True
print(panagram())

   

