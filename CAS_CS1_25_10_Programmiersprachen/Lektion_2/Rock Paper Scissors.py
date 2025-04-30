import random

computer_choice = random.randint(0, 2)

choices = ["scissors", "rock", "paper"]

user_choice = int(input("0 = Schere, 1 = Stein, 2 = Papier " ))
print("Computerchoice " + choices[computer_choice])

if computer_choice == 0:
    if user_choice == 0:
        print("Unentschieden")
    elif user_choice == 1:
        print("Du hast gewonnen")
    elif user_choice == 2:
        print("Du hast verloren")

elif  computer_choice == 1:
    if user_choice == 0:
        print("Du hast verloren")
    elif user_choice == 1:
        print("Unentschieden")
    elif user_choice == 2:
        print("Du hast gewonnen")

elif computer_choice == 2:
    if user_choice == 0:
        print("Du hast gewonnen")
    elif user_choice == 1:
        print("Du hast verloren")
    elif user_choice == 2:
        print("Unentschieden")