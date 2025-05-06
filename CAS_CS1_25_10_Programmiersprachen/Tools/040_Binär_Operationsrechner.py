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
                f"{format(rest, 'b').zfill(len(dividend_str))} - {divisor_str} = {format(diff, 'b').zfill(len(dividend_str))}")
            rest = diff
        else:
            quotient += "0"
            steps.append(f"{format(rest, 'b').zfill(len(dividend_str))} < {divisor_str} → 0")

    quotient += "."
    steps.append("--- Nachkommastellen ---")

    # Nachkommastellen
    for _ in range(nachkommastellen):
        rest <<= 1
        if rest >= divisor:
            quotient += "1"
            diff = rest - divisor
            steps.append(
                f"{format(rest, 'b').zfill(len(dividend_str))} - {divisor_str} = {format(diff, 'b').zfill(len(dividend_str))}")
            rest = diff
        else:
            quotient += "0"
            steps.append(f"{format(rest, 'b').zfill(len(dividend_str))} < {divisor_str} → 0")

    # Berechnung des Dezimalergebnisses
    dezimalergebnis = 0
    for i, bit in enumerate(quotient.replace(".", "")):
        if bit == "1":
            if i < quotient.index("."):
                dezimalergebnis += 2 ** (quotient.index(".") - 1 - i)
            else:
                dezimalergebnis += 2 ** -(i - quotient.index("."))

    # Formatierte Ausgabe
    textausgabe = f"📘 Schriftliche Division:\n{dividend_str} ÷ {divisor_str} = {quotient}\n"
    textausgabe += f"(dezimal: {dividend} ÷ {divisor} = {dezimalergebnis})\n\n"
    textausgabe += "\n".join(steps)

    return textausgabe


# Schriftliche Multiplikation Schritt für Schritt (Text)
def schriftliche_binärmultiplikation(bin1, bin2):
    dez1 = int(bin1, 2)
    dez2 = int(bin2, 2)

    teilergebnisse = []
    max_len = max(len(bin1), len(bin2))

    for i in range(len(bin2)):
        if bin2[-(i + 1)] == '1':
            teilergebnis = bin1 + '0' * i  # Verschieben je nach Stelle
            teilergebnisse.append(teilergebnis)
        else:
            teilergebnisse.append('0' * len(bin1) + '0' * i)

    ergebnis = 0
    for teilergebnis in teilergebnisse:
        ergebnis += int(teilergebnis, 2)

    dezimalergebnis = dez1 * dez2

    textausgabe = f"📘 Schriftliche Multiplikation:\n{bin1} * {bin2} = {format(ergebnis, 'b')}\n"
    textausgabe += f"(dezimal: {dez1} * {dez2} = {dezimalergebnis})\n\n"

    for i, teilergebnis in enumerate(teilergebnisse):
        textausgabe += f"Teilergebnis {i + 1}: {teilergebnis} (dezimal: {int(teilergebnis, 2)})\n"

    return textausgabe


# Schriftliche Addition Schritt für Schritt (Text)
def schriftliche_binäraddition(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    ergebnis = ""
    carry = 0
    steps = []

    for i in range(max_len - 1, -1, -1):
        a = int(bin1[i])
        b = int(bin2[i])
        summe = a + b + carry

        if summe == 0:
            ergebnis = "0" + ergebnis
            carry = 0
        elif summe == 1:
            ergebnis = "1" + ergebnis
            carry = 0
        elif summe == 2:
            ergebnis = "0" + ergebnis
            carry = 1
        elif summe == 3:
            ergebnis = "1" + ergebnis
            carry = 1

        steps.append(f"{bin1[i]} + {bin2[i]} + {carry} = {ergebnis}")

    if carry:
        ergebnis = "1" + ergebnis

    dezimalergebnis = int(bin1, 2) + int(bin2, 2)

    textausgabe = f"📘 Schriftliche Addition:\n{bin1} + {bin2} = {ergebnis}\n"
    textausgabe += f"(dezimal: {int(bin1, 2)} + {int(bin2, 2)} = {dezimalergebnis})\n\n"
    textausgabe += "\n".join(steps)

    return textausgabe


# Schriftliche Subtraktion Schritt für Schritt (Text)
def schriftliche_binärsubtraktion(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    ergebnis = ""
    borrow = 0
    steps = []

    for i in range(max_len - 1, -1, -1):
        a = int(bin1[i])
        b = int(bin2[i])

        if a - b - borrow == 1:
            ergebnis = "1" + ergebnis
            borrow = 0
        elif a - b - borrow == 0:
            ergebnis = "0" + ergebnis
            borrow = 0
        elif a - b - borrow == -1:
            ergebnis = "1" + ergebnis
            borrow = 1

        steps.append(f"{bin1[i]} - {bin2[i]} - {borrow} = {ergebnis}")

    dezimalergebnis = int(bin1, 2) - int(bin2, 2)

    textausgabe = f"📘 Schriftliche Subtraktion:\n{bin1} - {bin2} = {ergebnis}\n"
    textausgabe += f"(dezimal: {int(bin1, 2)} - {int(bin2, 2)} = {dezimalergebnis})\n\n"
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
        result = schriftliche_binäraddition(bin1, bin2)
    elif op == "-":
        result = schriftliche_binärsubtraktion(bin1, bin2)
    elif op == "*":
        result = schriftliche_binärmultiplikation(bin1, bin2)
    elif op == "/":
        result = schriftliche_binärdivision(bin1, bin2)
    else:
        result = "Ungültiger Operator"

    lösung.delete("1.0", tk.END)
    lösung.insert(tk.END, result)


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
