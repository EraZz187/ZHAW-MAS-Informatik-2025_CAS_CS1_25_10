age = int(input("Bitte gib dein Alter ein: "))

if age < 18:
    print("Achtung, der Nutzer ist jünger als 18")
elif age > 50:
    print("Achtung, der Nutzer viel zu Alt")
else:
    print("Altersprüfung bestanden")