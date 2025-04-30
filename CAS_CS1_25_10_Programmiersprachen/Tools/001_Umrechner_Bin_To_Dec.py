def bin_to_dec(binary_str):
    binary_str = binary_str.replace(" ", "").strip()  # Entfernt Leerzeichen
    if '.' in binary_str:
        int_part, frac_part = binary_str.split('.')
    else:
        int_part, frac_part = binary_str, ''

    decimal = 0

    # Integer part conversion
    power = len(int_part) - 1
    for digit in int_part:
        if digit not in ('0', '1'):
            print("Ungültige Eingabe! Bitte nur 0 oder 1 verwenden.")
            return None
        print(f"{digit} * 2^{power} = {int(digit) * (2 ** power)}")
        decimal += int(digit) * (2 ** power)
        power -= 1

    # Fractional part conversion
    for i, digit in enumerate(frac_part):
        if digit not in ('0', '1'):
            print("Ungültige Eingabe! Bitte nur 0 oder 1 verwenden.")
            return None
        power = -(i + 1)
        print(f"{digit} * 2^{power} = {int(digit) * (2 ** power)}")
        decimal += int(digit) * (2 ** power)

    return decimal

# Taking input from user
binary_input = input("Gib eine Binärzahl ein (z.B., 1100.0011): ")

# Calling the function and printing the result
result = bin_to_dec(binary_input)
if result is not None:
    print(f"Dezimal: {result}")
