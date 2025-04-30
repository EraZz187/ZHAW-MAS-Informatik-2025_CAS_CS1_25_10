zahlen = [0,0]

x = int(input("Geben Sie die erste Zahl ein "))
y = int(input("Geben Sie die zweite Zahl ein "))

while x != y:
    if x > y:
        x -= y
    else:
        y -= x

print("Der ggT Für " + str(x) + " und " + str(y) + " ist " + str(x))