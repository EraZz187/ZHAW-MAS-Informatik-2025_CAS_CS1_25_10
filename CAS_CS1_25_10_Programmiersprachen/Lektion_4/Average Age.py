Amount_People = int(input("Please tell me how much people "))

Min_Age = Max_Age = Sum_Age = Avr_Age = 0

i = 0
while i < Amount_People:
    i += 1
    age = int(input("Tell me the Age of the Person " + str(i) + " "))
    Sum_Age += age
    if  (age < Min_Age) or (Min_Age == 0):
        Min_Age = age

    if age > Max_Age:
        Max_Age = age

Avr_Age = Sum_Age / Amount_People

print("Lowest age:" + str(Min_Age) + ", Average age:" + str(Avr_Age) + ", Highest Age:" + str(Max_Age))


