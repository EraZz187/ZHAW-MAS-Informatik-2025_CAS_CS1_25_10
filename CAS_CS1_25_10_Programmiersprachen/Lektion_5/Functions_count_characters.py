def count_characters(values):
    letters = 0

    if isinstance(values, list):  # Ist values eine Liste?
        for e in values:
            letters += len(e)

    elif isinstance(values, str):  # Ist values ein String?
        letters += len(values)

    return letters


listOfStrings = ["efse", "51ef85", "wedsss"]

print(count_characters(listOfStrings))
print(count_characters("Hi"))