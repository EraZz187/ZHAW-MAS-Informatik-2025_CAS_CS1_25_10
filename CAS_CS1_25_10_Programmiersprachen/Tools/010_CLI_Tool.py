def dec_to_bin(number):
    if number == 0:
        return "0"
    s = ""
    while number > 0:
        print(f"{number} / 2 = {number // 2} Rest {number % 2}")
        s = str(number % 2) + s
        number //= 2
    return s

def bin_to_dec(binary_str):
    binary_str = binary_str.strip()
    decimal = 0
    power = len(binary_str) - 1
    for digit in binary_str:
        if digit not in "01":
            print("Ungültige Binärzahl!")
            return None
        val = int(digit)
        print(f"{digit} * 2^{power} = {val * (2 ** power)}")
        decimal += val * (2 ** power)
        power -= 1
    return decimal

def dec_to_oct(number):
    if number == 0:
        return "0"
    s = ""
    while number > 0:
        print(f"{number} / 8 = {number // 8} Rest {number % 8}")
        s = str(number % 8) + s
        number //= 8
    return s

def oct_to_dec(oct_str):
    oct_str = oct_str.strip()
    decimal = 0
    power = len(oct_str) - 1
    for digit in oct_str:
        if digit not in "01234567":
            print("Ungültige Oktalzahl!")
            return None
        val = int(digit)
        print(f"{digit} * 8^{power} = {val * (8 ** power)}")
        decimal += val * (8 ** power)
        power -= 1
    return decimal

def dec_to_hex(number):
    if number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    s = ""
    while number > 0:
        rest = number % 16
        print(f"{number} / 16 = {number // 16} Rest {rest} (Hex: {hex_chars[rest]})")
        s = hex_chars[rest] + s
        number //= 16
    return s

def hex_to_dec(hex_str):
    hex_str = hex_str.strip().upper()
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    power = len(hex_str) - 1
    for digit in hex_str:
        if digit not in hex_chars:
            print("Ungültige Hexadezimalzahl!")
            return None
        val = hex_chars.index(digit)
        print(f"{digit} (={val}) * 16^{power} = {val * (16 ** power)}")
        decimal += val * (16 ** power)
        power -= 1
    return decimal

# Hauptmenü
while True:
    print("\nWähle den Umrechnungsmodus:")
    print("1. Dezimal → Binär")
    print("2. Binär → Dezimal")
    print("3. Dezimal → Oktal")
    print("4. Oktal → Dezimal")
    print("5. Dezimal → Hexadezimal")
    print("6. Hexadezimal → Dezimal")
    print("0. Beenden")

    wahl = input("Deine Auswahl: ")

    if wahl == "1":
        zahl = int(input("Dezimalzahl eingeben: "))
        print("Binär:", dec_to_bin(zahl))

    elif wahl == "2":
        bin_zahl = input("Binärzahl eingeben: ")
        result = bin_to_dec(bin_zahl)
        if result is not None:
            print("Dezimal:", result)

    elif wahl == "3":
        zahl = int(input("Dezimalzahl eingeben: "))
        print("Oktal:", dec_to_oct(zahl))

    elif wahl == "4":
        oct_zahl = input("Oktalzahl eingeben: ")
        result = oct_to_dec(oct_zahl)
        if result is not None:
            print("Dezimal:", result)

    elif wahl == "5":
        zahl = int(input("Dezimalzahl eingeben: "))
        print("Hexadezimal:", dec_to_hex(zahl))

    elif wahl == "6":
        hex_zahl = input("Hexadezimalzahl eingeben: ")
        result = hex_to_dec(hex_zahl)
        if result is not None:
            print("Dezimal:", result)

    elif wahl == "0":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Auswahl. Bitte nochmal versuchen.")