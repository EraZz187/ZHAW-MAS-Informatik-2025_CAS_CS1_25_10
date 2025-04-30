def dec_to_hex(number):
    hex_chars = "0123456789ABCDEF"

    # Ganzzahliger Teil
    int_part = int(number)
    frac_part = number - int_part

    solution_steps = []
    solution_steps.append(f"--- Umwandlung von {number} in Hexadezimal ---\n")

    # GANZZAHLENBEREICH
    solution_steps.append(">> Vorkommateil:")
    if int_part == 0:
        int_result = "0"
        solution_steps.append("0 ist direkt 0 in Hexadezimal.")
    else:
        int_result = ""
        n = int_part
        while n > 0:
            rest = n % 16
            hex_digit = hex_chars[rest]
            solution_steps.append(f"{n} / 16 = {n // 16} Rest {rest} → {hex_digit}")
            int_result = hex_digit + int_result
            n = n // 16
        solution_steps.append(f"Ergebnis (vorn): {int_result}")

    # KOMMABEREICH
    frac_result = ""
    count = 0
    solution_steps.append("\n>> Nachkommabereich (max. 5 Stellen):")
    if frac_part == 0:
        solution_steps.append("Kein Nachkommaanteil vorhanden.")
    else:
        while frac_part > 0 and count < 5:
            frac_part *= 16
            digit = int(frac_part)
            hex_digit = hex_chars[digit]
            solution_steps.append(f"16 * Rest = {frac_part} → Ganzzahl = {digit} → {hex_digit}")
            frac_result += hex_digit
            frac_part -= digit
            count += 1
        solution_steps.append(f"Ergebnis (nach Komma): {frac_result}")

    # Gesamtergebnis
    if frac_result:
        result = f"{int_result}.{frac_result}"
    else:
        result = int_result

    solution_steps.append(f"\n>> Gesamtergebnis: {result}")
    return "\n".join(solution_steps)


try:
    user_input = input("Gegebene Dezimalzahl (mit oder ohne Komma): ").replace(",", ".")
    number = float(user_input)
    print(dec_to_hex(number))
except ValueError:
    print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
