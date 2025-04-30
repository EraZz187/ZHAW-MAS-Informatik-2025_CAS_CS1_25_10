def dec_to_oct(number):
    int_part = int(number)
    frac_part = number - int_part

    # Vorkommateil
    if int_part == 0:
        int_result = "0"
    else:
        int_result = ""
        n = int_part
        while n > 0:
            rest = n % 8
            print(f"{n} / 8 = {n // 8} Rest {rest}")
            int_result = str(rest) + int_result
            n = n // 8
        int_result = formatString(int_result)

    # Nachkommateil
    frac_result = ""
    count = 0
    print("Nachkommabereich:")
    while frac_part > 0 and count < 5:  # bis zu 5 Stellen
        frac_part *= 8
        digit = int(frac_part)
        frac_result += str(digit)
        print(f"8 * Rest = {frac_part} => Ganzzahl = {digit}")
        frac_part -= digit
        count += 1

    if frac_result:
        return f"{int_result.strip()} , {frac_result}"
    else:
        return f"{int_result.strip()}"

def formatString(value):
    while len(value) % 3 != 0:
        value = "0" + value

    s = ""
    for i in range(len(value)):
        s += value[i]
        if (i + 1) % 3 == 0 and i != len(value) - 1:
            s += " "
    return s

try:
    user_input = input("Gegebene Dezimalzahl (mit oder ohne Komma): ").replace(",", ".")
    number = float(user_input)
    print("Oktalzahl:", dec_to_oct(number))
except ValueError:
    print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
