f = open("zahlen.txt","r")
val = 0

for line in f:
    val += float(line)
f.close()
print(val)
