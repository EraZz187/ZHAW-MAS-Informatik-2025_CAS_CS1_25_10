"""Lists can be created in different ways:
You can add a value to a list dynamically (append adds to the
end of the list):"""

first_list = [] # creates an empty list
second_list = [1, 2, 3, 4] # creates a list with 1,2,3 and 4
third_list = ["abc","def"] # creates a list with "abc" and "def"
print(third_list) # prints ["abc","def"]

first_list = ["Steve McQueen"] # creates a list with one value
first_list.append("Peter Fonda") # Adds the string "Peter Fonda"
print(first_list) # prints ["Steve McQueen","Peter Fonda"]
first_list.append("Paul Newman") # Adds the string "Paul Newman"
print(first_list) # prints ["Steve McQueen","Peter Fonda","Paul Newman"]

second_list = [1, 2, 3, 4] # creates a list with 1,2,3 and 4
print(len(second_list)) # prints the length of the list,
                        # in this case 4
print(second_list[0]) # prints the first value of the list,
                      # in this case 1
del(second_list[1]) # deletes the element with index 1
                    # (note that we start counting with zero)
print(second_list) # prints [1,3,4]