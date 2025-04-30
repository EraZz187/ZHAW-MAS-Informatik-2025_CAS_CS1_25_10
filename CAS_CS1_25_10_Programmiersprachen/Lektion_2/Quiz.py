answer = input("Wie viele Stunden hat der Tag? ")

if int(answer) == 24:
    print("Korrekt")

elif abs(int(answer) - 24) < 3:
    print("Resultat ist fast richtig")

else:
    print("Leider Falsch")
