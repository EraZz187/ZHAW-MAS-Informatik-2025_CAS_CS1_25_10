r = open("passwords.txt","r")
w = open("passwordsValid", "w")

lineCount = 0
validLineCount = 0

for line in r:
    lineCount += 1
    lowest_number = line[:line.index("-")]
    highest_number = line[len(lowest_number)+1:line.index(" ")]
    character = line[line.index(" ") +1:line.index(":")]

    #Debuging
    #print(lowest_number + ":" + highest_number + ":" + character)

    if (line.count(character) >= int(lowest_number)) and (line.count(character) <= int(highest_number)):
        w.write("Nr." + str(lineCount) + "_  " + line)
        validLineCount += 1

print("Valid lines: " + str(validLineCount))

r.close()
w.close()