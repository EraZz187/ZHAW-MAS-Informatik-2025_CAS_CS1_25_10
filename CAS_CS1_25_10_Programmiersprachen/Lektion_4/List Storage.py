entered_Number = 0
nums = []

while entered_Number >= 0:
    entered_Number = int(input("Please enter a positive number "))
    nums.append(entered_Number)

print("You entered: " + str(nums))