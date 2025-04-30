date = input("please enter a date: ") #dd.mm.yyyy

q = int(date[:2])
m = int(date[3:5])
J = int(date[6:8])
K = int(date[8:])

h = (q+ int(13 * (m + 1) / 5) + K + int(K / 4) + int(J / 4) - 2*J) % 7

weekdays = "SaSoMoDiMiDoFr"
weekdays_eng = "SatSunMonTueWenThrFri"

print("0 = Samstag, 1 = Sonntag, 2 = Montag, 3 = Dienstag, 4 = Mittwoch, 5 = Donerstag, 6 = Freitag")
print("DayOfWeek: " + weekdays[h*2:2*h+2])
print("DayOfWeek: " + weekdays_eng[h*3:3*h+3])

