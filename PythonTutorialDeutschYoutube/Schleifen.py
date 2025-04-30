from sqlalchemy.sql.base import elements

import Funktionen

counter = 5
while counter < 10:
    print("While-Schleife: " + str(counter))
    counter += 1

fruitsList = ["apple", "banana", "cherry"]
for fruits in fruitsList:
    print("For-Schleife: " + fruits)

print(fruitsList)

for element in "Test":
    print(element)

print("")

for element in range(10):
    print(element)

print("")

for element in range(5, 10):
    print(element)