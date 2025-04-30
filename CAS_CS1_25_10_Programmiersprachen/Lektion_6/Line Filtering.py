r = open("passwords.txt","r")
w = open("filtered_passwords.txt ", "w")

for line in r:

    if (line[:2] == "1-"):
        w.write(line)

r.close()
w.close()