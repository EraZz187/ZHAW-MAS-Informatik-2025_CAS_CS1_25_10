import tkinter as tk


# Schriftliche Division Schritt für Schritt (Text)
def schriftliche_binärdivision(dividend_str, divisor_str, nachkommastellen=8):
    dividend = int(dividend_str, 2)
    divisor = int(divisor_str, 2)

    if divisor == 0:
        return "Fehler: Division durch 0"

    steps = []
    quotient = ""
    rest = 0
    dividend_bin = dividend_str
    idx = 0

    # Ganze Zahlenteile
    while idx < len(dividend_bin):
        rest = (rest << 1) | int(dividend_bin[idx])
        idx += 1
        if rest >= divisor:
            quotient += "1"
            diff = rest - divisor
            steps.append(
                f"{format(rest, 'b').zfill(len(divisor_str))} - {divisor_str} = {format(diff, 'b').zfill(len(divisor_str))}")
            rest = diff
        else:
            quotient += "0"
            steps.append(f"{format(rest, 'b').zfill(len(divisor_str))} < {divisor_str} → 0")

    quotient += "."
    steps.append("--- Nachkommastellen ---")

    # Nachkommastellen
    for _ in range(nachkommastellen):
        rest <<= 1
        if rest >= divisor:
            quotient += "1"
            diff = rest - divisor
            steps.append(
                f"{format(rest, 'b').zfill(len(divisor_str))} - {divisor_str} = {format(diff, 'b').zfill(len(divisor_str))}")
            rest = diff
        else:
            quotient += "0"
            steps.append(f"{format(rest, 'b').zfill(len(divisor_str))} < {divisor_str} → 0")

    # Korrekte Berechnung des Dezimalwerts
    # Binärzahl in Dezimal umwandeln und den richtigen Dezimalwert berechnen
    if '.' in quotient:
        whole_part, fractional_part = quotient.split('.')
    else:
        whole_part = quotient
        fractional_part = '0'

    # Ganze Zahl als Dezimalwert berechnen
    dezimal_whole = int(whole_part, 2)

    # Nachkommastellen als Dezimalwert berechnen
    dezimal_fraction = 0
    for i, bit in enumerate(fractional_part):
        dezimal_fraction += int(bit) * (2 ** -(i + 1))

    dezimalergebnis = dezimal_whole + dezimal_fraction

    textausgabe = f"📘 Schriftliche Division:\n{dividend_str} ÷ {divisor_str} = {quotient}\n"
    textausgabe += f"(dezimal: {dividend} ÷ {divisor} = {dezimalergebnis:.8f})\n\n"
    textausgabe += "\n".join(steps)

    return textausgabe


# GUI-Funktion
def berechne():
    bin1 = eingabe1.get()
    bin2 = eingabe2.get()
    op = operator.get()

    try:
        dez1 = int(bin1, 2)
        dez2 = int(bin2, 2)
    except ValueError:
        lösung.delete("1.0", tk.END)
        lösung.insert(tk.END, "Ungültige Binärzahl!")
        return

    if op == "+":
        result = bin(dez1 + dez2)[2:]
        lösung_text = f"{bin1} + {bin2} = {result}"
    elif op == "-":
        result = bin(dez1 - dez2)[2:] if dez1 >= dez2 else "-" + bin(dez2 - dez1)[2:]
        lösung_text = f"{bin1} - {bin2} = {result}"
    elif op == "*":
        result = bin(dez1 * dez2)[2:]
        lösung_text = f"{bin1} * {bin2} = {result}"
    elif op == "/":
        lösung_text = schriftliche_binärdivision(bin1, bin2)
    else:
        lösung_text = "Ungültiger Operator"

    lösung.delete("1.0", tk.END)
    lösung.insert(tk.END, lösung_text)


# GUI Aufbau
fenster = tk.Tk()
fenster.title("Binär-Operationsrechner")

tk.Label(fenster, text="Erste Binärzahl:").grid(row=0, column=0)
eingabe1 = tk.Entry(fenster)
eingabe1.grid(row=0, column=1)

tk.Label(fenster, text="Operator (+ - * /):").grid(row=1, column=0)
operator = tk.Entry(fenster)
operator.grid(row=1, column=1)

tk.Label(fenster, text="Zweite Binärzahl:").grid(row=2, column=0)
eingabe2 = tk.Entry(fenster)
eingabe2.grid(row=2, column=1)

tk.Button(fenster, text="Berechne", command=berechne).grid(row=3, columnspan=2)

lösung = tk.Text(fenster, height=20, width=60)
lösung.grid(row=4, columnspan=2)

fenster.mainloop()
