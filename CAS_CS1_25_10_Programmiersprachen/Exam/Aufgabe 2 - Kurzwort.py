def kurzwort(array_of_words):
    shortest_word = ""
    counter = 0

    for word in array_of_words:
        if len(word) < len(shortest_word) or shortest_word == "":
            shortest_word = word

    for word in array_of_words:
        if len(word) == len(shortest_word):
            counter += 1

    if counter > 1:
        for word in array_of_words:
            if len(word) == len(shortest_word):
                shortest_word = str(array_of_words.index(shortest_word))
                return shortest_word

    return str(array_of_words.index(shortest_word))

wordlist1 = ["der", "in", "viel", "wenig"]
wordlist2 = ["gestern", "morgen", "heute"]
wordlist3 = ["alpha", "beta", "gamma", "delta", "omega", "zeta"]

print(kurzwort(wordlist2)) #Beginnend bei 0