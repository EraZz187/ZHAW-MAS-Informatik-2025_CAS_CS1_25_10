import random

input("Press any Key to roll the dices!")

user_dices = [random.randint(1, 6),random.randint(1, 6)]
computer_dices = [random.randint(1, 6),random.randint(1, 6)]

if user_dices[0] == user_dices[1]:
    result_user = user_dices[0] * 20
else:
    result_user = (user_dices[0] + user_dices[1])

if computer_dices[0] == computer_dices[1]:
    result_computer = computer_dices[0] * 20
else:
    result_computer = (computer_dices[0] + computer_dices[1])

print("Dices computer: " + str(computer_dices[0]) +", "+ str(computer_dices[1]) + " sum: " + str(result_computer))
print("Dices user: " + str(user_dices[0]) +", "+ str(user_dices[1]) + " sum: " + str(result_user))

if result_user > result_computer:
    print("You Won!")
elif result_computer > result_user:
    print("You Lost!")
else:
    print("Tied!")


