#Concatenation string1 + string2:
s = "Hello" + "World" # now contains "HelloWorld" (without space)
# Get length of a string len(string1):
s = len('Hello') # 5
#Repeat string string1 * n:
s = '.' * 5 # "....."
#Get character at index 5 (0-based!)
string1 = 'abcdefgh'
s = string1[5] # "f"
#Get substring with slicing string1[start:stop]:
string1 = "abcdefgh"
s = string1[:5] # "abcde"
print(s)

name = input("Bitte geben Sie einen Namen ein: ")
nameStar = "*" + name + "*"
print(nameStar)
print("Zeichen in Name: " + str(len(name)))
print(name * 2)
print(name[2])
print(name[4:6])