def count_letters(text):
    result = [0] * 26
    for c in text:
        # print(c)
        if c.isalpha():
            c = ord(c.upper()) - 65
            if c >= 0 and c <= 25:
                result[c] += 1

    return result


numbers = count_letters("Ein kurzer Test")
print(numbers)


def language(text):
    result = count_letters(text)
    num_letters = sum(result)

    percent_e = result[4] / num_letters * 100
    percent_t = result[19] / num_letters * 100
    percent_o = result[14] / num_letters * 100

    print("e:", percent_e, "o:", percent_o, "t:", percent_t)

    nearby_e = (17.40 + 12.702) / 2 - percent_e
    nearby_o = (2.51 + 7.507) / 2 - percent_o
    nearby_t = (6.15 + 9.056) / 2 - percent_t
    print("ne:", nearby_e, "no:", nearby_o, "nt:", nearby_t)

    german_english = 0
    if nearby_e > 1:
        german_english -= 1
    if nearby_e < -1:
        german_english += 1

    if nearby_o > 1:
        german_english += 1
    if nearby_o < -1:
        german_english -= 1

    if nearby_t > 1:
        german_english += 1
    if nearby_t < -1:
        german_english -= 1
    print(german_english)
    result = ""
    if german_english > 2 or german_english < -2:
        result += "VERY SURE IT'S "
    elif german_english > 1 or german_english < -1:
        result += "QUITE SURE IT'S "
    else:
        result += "NOT SURE BUT WOULD GUESS IT'S "
    if german_english > 0:
        result += "GERMAN"
    else:
        result += "ENGLISCH"

    return result


#print(language("Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a batteries included language due to its comprehensive standard library. Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[32] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting and was discontinued with version 2.7.18 in 2020.[33] Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3. "))
print(language("During his first decade as a director Ford worked on dozens of features (including many westerns) but only ten of the more than sixty silent films he made between 1917 and 1928 still survive in their entirety.[16] However, prints of several Ford 'silents' previously thought lost have been rediscovered in foreign film archives over recent years—in 2009 a trove of 75 Hollywood silent films was rediscovered in the New Zealand Film Archive, among which was the only surviving print of Ford's 1927 silent comedy Upstream.[17] The print was restored in New Zealand by the Academy of Motion Picture Arts & Sciences before being returned to America, where it was given a repremiere at the Samuel Goldwyn Theater in Beverly Hills on August 31, 2010, featuring a newly commissioned score by Michael Mortilla. Throughout his career, Ford was one of the busiest directors in Hollywood, but he was extraordinarily productive in his first few years as a director—he made ten films in 1917, eight in 1918 and fifteen in 1919—and he directed a total of 62 shorts and features between 1917 and 1928, although he was not given a screen credit in most of his earliest films. There is some uncertainty about the identity of Ford's first film as director—film writer Ephraim Katz notes that Ford might have directed the four-part film Lucille the Waitress as early as 1914[19]—but most sources cite his directorial début as the silent two-reeler The Tornado, released in March 1917. According to Ford's own story, he was given the job by Universal boss Carl Laemmle who supposedly said, Give Jack Ford the job—he yells good. The Tornado was quickly followed by a string of two-reeler and three-reeler quickies—The Trail of Hate, The Scrapper, The Soul Herder and Cheyenne's Pal; these were made over the space of a few months and each typically shot in just two or three days; all are now presumed lost. The Soul Herder is also notable as the beginning of Ford's four-year, 25-film association with veteran writer-actor Harry Carey,[20] who (with Ford's brother Francis) was a strong early influence on the young director, as well as being one of the major influences on the screen persona of Ford's protege John Wayne. Carey's son Harry Dobe Carey Jr., who also became an actor, was one of Ford's closest friends in later years and featured in many of his most celebrated westerns. "))
#print(language("Nach viel Widerspruch gegen den vermeldeten Fund des Moleküls Phosphin (PH3) in der Atmosphäre der Venus kommt nun Unterstützung aus unerwarteter Richtung: Eine 1978 durch die Atmosphäre des Planeten geflogene NASA-Sonde hat damals Spuren des Moleküls gefunden, haben Forscher bei einer Analyse der längst archivierten Daten herausgefunden. Damit liefern sie eine erste unabhängige Bestätigung des Sensationsfunds und dürften die Kontroverse neu entfachen. Immerhin hatte es geheissen, dass das Molekül auf nicht-biologischem Weg dort nicht entstehen dürfte. Ausser Phosphin wurden nun auch Hinweise auf andere biologisch relevante Chemikalien gefunden."))
#print(language("Die Buchstabenhäufigkeit wird in der Entschlüsselung von Substitutionsverfahren in der Kryptoanalyse sowie in der Datenkompression und -kodierung benutzt. Bei einfachen Verschlüsselungsverfahren wie bei der Cäsarchiffre kann ein Geheimtext alleine durch Häufigkeitsanalyse entschlüsselt werden. Dabei werden die Häufigkeiten der einzelnen Zeichen im Geheimtext festgestellt und dann mit der Häufigkeit der Zeichen in einem Klartext der vermuteten Sprache verglichen. Nun werden die Buchstaben des Geheimtextes durch die normalen Buchstaben gleicher Häufigkeit ersetzt. Der häufigste Buchstabe des Geheimtextes entspricht dann zum Beispiel dem Klartextbuchstaben e. Diese Methode ist offensichtlich für längere zu entschlüsselnde Texte besonders gut geeignet, weil die statistische Abweichung der gefundenen Buchstabenhäufigkeit von der zu erwartenden Häufigkeit geringer wird."))


