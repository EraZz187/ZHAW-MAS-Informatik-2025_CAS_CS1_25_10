def shift_chars(word, factor):
    newWord= ""

    for i in word:
        n = ord(i)
        n += factor
        newWord += chr(n)

    return newWord

print(shift_chars("HALLO", 1))
