def count_words(text):
    # split(p): splits the string by the given split symbol p
    # and returns all parts between p as elements in
    # a list

    words = text.split(" ")
    return len(words)


def count_sentences(text):
    # replace(p1,p2): replaces all characters of p1
    # in the string with p2

    text = text.replace("?", ".")
    text = text.replace("!", ".")

    sentences = text.split(".")
    print(sentences)
    return len(sentences)


text = input("Bitte geben Sie einen Text ein:")
print(count_words(text))
print(count_sentences(text))