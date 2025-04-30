age = int(input("Please enter your age: "))
if age >= 18:
    # this block (only one line) will be executed
    # if the age of the user is >= 18
    print("you are of legal age")
else:
    # this block (only one line) will be executed
    # if the age of the user is < 18
    print("you are a minor")

if age >= 65:
    print("you are a senior")
elif age >= 18:
    print("you aren't a senior but of legal age")
else:
    print("you aren't a senior")