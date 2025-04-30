#f = open("C:\\Users\\becir\\Documents\\TestFile.txt","w") # open a file to write to
f = open("t.txt","w") # open a file to write to
# the file is created in the same directory
# as the program. If the file does not exist it
# is created. If it exists, it is overwritten
f.write("Henry Fonda\nPaul Newman\nJohn Wayne\n")
# writes a string with three lines (2 times \n).
f.close() # closes the file
