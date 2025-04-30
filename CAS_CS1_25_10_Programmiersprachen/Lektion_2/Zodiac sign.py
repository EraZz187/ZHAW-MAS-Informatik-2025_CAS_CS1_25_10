date = input("please enter a date: ") #dd.mm.yyyy

day = int(date[:2])
month = int(date[3:5])
year = int(date[6:])

if month == 4:
    if day >= 21 and day <= 30:
        print("Ihr Sternzeichen lautet: Taurus - Stier")
elif month == 5:
    if day >= 0 and day <= 20:
        print("Ihr Sternzeichen lautet: Taurus - Stier")
else:
    print("Ihr Sternzeichen lautet: Unbekannt")