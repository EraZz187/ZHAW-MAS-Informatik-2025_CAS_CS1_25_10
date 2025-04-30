import datetime
from dateutil.parser import parse

debug = 0

r = open("times.txt", "r")

linesCount = 0
totalTimes = 0

for lines in r:
    linesCount += 1

    startDT = datetime.datetime
    endDT = datetime.datetime

    temp = lines.split("-")
    startDT = parse(temp[0])

    temp = lines.split(";")
    temp += temp[1].split("-")
    temp = temp[0] + " " +temp[3]
    endDT = parse(temp)

    workinTimes = endDT - startDT
    totalTimes += workinTimes.seconds

    print(startDT)
    print(endDT)
    print(workinTimes)

avgTimes = (totalTimes / linesCount) / 60

print("Average working Time: " + str(avgTimes) + " min. per Day")

