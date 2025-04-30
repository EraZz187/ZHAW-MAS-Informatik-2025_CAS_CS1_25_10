"""In this game, two players play on a board with 30 squares.
The goal is to reach the final square first. Each square has a
number from 0 to 3. These numbers are chosen randomly.
The number of the first square is always 0.
Start this game by storing the board (of 30 squares) in a list.
Add a random number between 0 and 3 to each square.
Output the list:"""

import random

squares = []
uPositionNr = sPositionNr = cPositionNr = 0

for i in range(0,29):
    squares.append(random.randint(0, 3))

t_txt: str = ""

for i in range(0, 29):
    t_txt += str(squares[i])
    t_txt += "|"

t_txt = t_txt[:len(t_txt) -1]

print(squares)

while uPositionNr < 29 and sPositionNr < 29 and cPositionNr < 29:

    # print(squares)

    # Racetrack 2
    """Improve the racetrack output:"""
    #t_txt: str = ""

    #for j in squares:
    #    t_txt += str(squares[j])
    #    t_txt += "|"

    #t_txt = t_txt[:len(t_txt) -1]
    print(t_txt)

    # Racetrack 3
    """It is time to add some game logic. Each player has a position
    on the track. Add two variables that store the current
    position of each player and use these values in the output:"""

    #uPositionNr = (int(input("User 1 position: ")))
    #cPositionNr = (int(input("User 2 position: ")))

    u_txt = ""

    for i in range(0, 57):
        u_txt += "_"

    c_txt = s_txt = u_txt

    print()
    print(u_txt[:uPositionNr * 2] + "U" + u_txt[uPositionNr * 2 + 1:])
    print(s_txt[:sPositionNr * 2] + "S" + s_txt[sPositionNr * 2 + 1:])
    print(c_txt[:cPositionNr * 2] + "C" + c_txt[cPositionNr * 2 + 1:])
    print(t_txt)

    # Racetrack 4
    """Each player can either roll a coin and move either 1 or 2
    steps forward, or it can move as many fields forward as the
    number of the current field. The computer player should
    always throw a coin. The human player should decide.
    Implement this logic and finish the game."""

    ucoin = random.randint(1, 2)
    scoin = random.randint(1, 2)
    ccoin = random.randint(1, 2)

    uchoice = int(input("U for Fields type 1 and for Coin type 2 "))

    if uchoice == 1:
        uPositionNr += squares[uPositionNr]

    elif uchoice == 2:
        uPositionNr += ucoin

    if uPositionNr >= 29:
        uPositionNr = 29
        print("U Won!!!")

    schoice = int(input("S for Fields type 1 and for Coin type 2 "))

    if schoice == 1:
        sPositionNr += squares[sPositionNr]

    elif schoice == 2:
        sPositionNr += scoin

    if sPositionNr >= 29:
        sPositionNr = 29
        print("S Won!!!")

    cPositionNr += ccoin

    if cPositionNr >= 29:
        cPositionNr = 29
        print("C Won!!!")