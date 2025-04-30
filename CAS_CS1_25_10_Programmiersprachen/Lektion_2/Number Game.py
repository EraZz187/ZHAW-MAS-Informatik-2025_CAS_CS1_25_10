answer = input("Ist die Nummer grösser als 5? ")
if answer == "Ja":
    answer = input("Ist die Nummer grösser als 7? ")
    if answer == "Ja":
        answer = input("Ist die Nummer grösser als 9? ")
        if answer == "Ja":
            print("Sie haben die 10 ausgewählt")
        else:
            answer = input("Ist die Nummer die 8? ")
            if answer == "Ja":
                print("Sie haben die 8 ausgewählt")
            else:
                print("Sie haben die 9 ausgewählt")
    else:
        answer = input("Ist die Nummer die 6? ")
        if answer == "Ja":
            print("Sie haben die 6 ausgewählt")
        else:
            print("Sie haben die 7 ausgewählt")