f = open("t.txt","r") # opens a file to read from.
# The program crashes if the file does not exist.

for line in f:
    print(line[:-1])
    # will print
    #Henry Fonda
    #Paul Newman
    #John Wayne
    # line still contains the ending '\n'. If not removed
    # (with [:-1]), it would result in an empty line when
    # printed.
f.close() # closes the file
