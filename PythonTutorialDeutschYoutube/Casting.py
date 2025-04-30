value1 = input("Erste Zahl eingeben: ")
value2 = input("Zweite Zahl eingeben: ")

type_of_value = type(value1)

print(type_of_value)

print ("Addition ohne Type-Casting: " + value1 + value2)
print ("Addition mit Type-Casting: " + str(int(value1) + int(value2)))

