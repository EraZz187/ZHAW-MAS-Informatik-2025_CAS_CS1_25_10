def oct_to_dec(octal_str):
    # Format anpassen
    octal_str = octal_str.replace(" ", "").replace(",", ".")

    if "." in octal_str:
        int_part_str, frac_part_str = octal_str.split(".")
    else:
        int_part_str, frac_part_str = octal_str, ""

    # Vorkommateil berechnen
    int_result = 0
    for i, digit in enumerate(reversed(int_part_str)):
        int_result += int(digit) * (8 ** i)

    # Nachkommateil berechnen
    frac_result = 0
    for i, digit in enumerate(frac_part_str):
        frac_result += int(digit) / (8 ** (i + 1))

    return int_result + frac_result


try:
    user_input = input("Gegebene Oktalzahl (mit oder ohne Komma): ")
    dezimal = oct_to_dec(user_input)
    print("Dezimalzahl:", dezimal)
except ValueError:
    print("Ungültige Eingabe. Bitte eine gültige Oktalzahl eingeben.")
