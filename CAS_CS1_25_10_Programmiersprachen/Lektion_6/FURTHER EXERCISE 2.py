import random

from sympy import false

diceImage = ["", "\u2680" , "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]


sumDiceOne = 0
sumDiceTwo = 0
countPairs = 0
countFollowingPairs = 0
averageNumber = 0
FollowingPairs = false

for i in range(1000):

    d1 = (random.randint(1, 6))
    d2 = (random.randint(1, 6))

    print(str(d1) + diceImage[d1] + ":" + str(d2) + diceImage[d2])

    sumDiceOne += d1
    sumDiceTwo += d2

    if (d1 == d2):
        countPairs += 1
        if (FollowingPairs):
            countFollowingPairs += 1
    else:
        FollowingPairs = false

    if (d1 == d2):
        FollowingPairs = True

print("Total d1: " + str(sumDiceOne))
print("Total d2: " + str(sumDiceTwo))
print("Total Pairs: " + str(countPairs))
print("TotalFollowingPairs: " + str(countFollowingPairs))




