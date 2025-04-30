def hex_to_dec(hex_str):
    hex_str = hex_str.replace(" ", "").replace(",", ".").upper()
    hex_chars = "0123456789ABCDEF"
    solution_steps = []

    solution_steps.append(f"--- Umwandlung von {hex_str} in Dezimal ---\n")

    if "." in hex_str:
        int_part_str, frac_part_str = hex_str.split(".")
    else:
        int_part_str, frac_part_str = hex_str, ""

    # Vorkommateil berechnen
    solution_steps.append(">> Vorkommateil:")
    int_result = 0
    for i, char in enumerate(reversed(int_part_str)):
        if char not in hex_chars:
            raise ValueError(f"Ungültiges Zeichen im Vorkommateil: {char}")
        value = hex_chars.index(char)
        power = 16 ** i
        contribution = value * power
        solution_steps.append(f"{char} = {value} → {value} * 16^{i} = {contribution}")
        int_result += contribution
    solution_steps.append(f"Summe Vorkommateil: {int_result}")

    # Nachkommateil berechnen
    solution_steps.append("\n>> Nachkommabereich:")
    frac_result = 0
    for i, char in enumerate(frac_part_str):
        if char not in hex_chars:
            raise ValueError(f"Ungültiges Zeichen im Nachkommabereich: {char}")
        value = hex_chars.index(char)
        divisor = 16 ** (i + 1)
        contribution = value / divisor
        solution_steps.append(f"{char} = {value} → {value} / 16^{i+1} = {contribution}")
        frac_result += contribution

    solution_steps.append(f"Summe Nachkommabereich: {frac_result}")

    total = int_result + frac_result
    solution_steps.append(f"\n>> Gesamtergebnis: {total}")
    return "\n".join(solution_steps)

try:
    user_input = input("Gegebene Hexadezimalzahl (mit oder ohne Komma): ")
    print(hex_to_dec(user_input))
except ValueError as e:
    print(f"Fehler: {e}")
