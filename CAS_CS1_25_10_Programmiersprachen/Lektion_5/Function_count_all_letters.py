


def count_all_letters(text):
    list1 = []
    list2 = []
    list3 = []
    oldhex = 0

    for i in text:
        if i.isalpha():
            hex = ord(i.upper())
            list1.append(hex)

    list1.sort()

    for i in list1:
        if i != oldhex:
            list2.append(list1.count(i))

        oldhex = i

    for i in list1:
        if list3.count(chr(i)) == 0:
            list3.append(chr(i))

    print(list1)
    print(list2)
    print(list3)

count_all_letters("Hello")





