import random

from spyder.utils.snippets.nodes import ElseNode
from sympy import false

min_value = int(input("Min: "))
max_value = int(input("Max: "))
n = int(input("n: "))

def listToString (list):
    strPrint = ""
    for i in range(len(list)):
        strPrint += str(list[i])
    return strPrint

randomValues = []
list1 = []
list2 = []
list3 = []

for i in range(n):
    randomValues.append(random.randint(min_value,max_value))

#print(randomValues)

for i in range(len(randomValues)):
    nr = nl = 0

    if (i > 0):
        nl = randomValues[i-1]
    if (i < len(randomValues) - 1):
        nr = randomValues[i+1]

    sum = nl + randomValues[i] + nr
    list1.append(sum)

    if (sum) <= max_value:
        list2.append(sum)
    else:
        list2.append(0)
same = False

for i in range(len(randomValues)):
    if same:
        list3.append("+")
    else:
        list3.append("_")

    same = True

    if i > 0 and i < len(randomValues) - 2:
        if randomValues[i -1] != randomValues[i]:
            same = False
        if randomValues[i] != randomValues[i +1]:
            same = False
        if randomValues[i +1] != randomValues[i +2]:
            same = False
    else:
        same = False

print("Random: " + listToString(randomValues))
print("Gleich: " + listToString(list3))
print("Summe:  " + listToString(list1))
print("Limit:  " + listToString(list2))