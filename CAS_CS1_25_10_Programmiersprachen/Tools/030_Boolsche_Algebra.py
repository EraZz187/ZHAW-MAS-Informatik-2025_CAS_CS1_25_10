import tkinter as tk
from sympy import symbols, simplify_logic, to_dnf
from sympy.parsing.sympy_parser import parse_expr

# Definiere gültige Variablen
a, b, c, d, x, y, z = symbols('a b c d x y z')

def simplify_boolean():
    expr_str = entry.get()
    steps = []

    try:
        # Eingabe umwandeln in sympy-kompatible Notation
        expr_str = expr_str.replace('+', '|').replace('*', '&').replace('-', '~')
        expr = parse_expr(expr_str, evaluate=False)

        steps.append("1️⃣ Ausgangsausdruck:")
        steps.append(f"🔹 {expr}")

        # Schritt 1: Distributive Normalform (DNF)
        dnf_expr = to_dnf(expr, simplify=False)
        if expr != dnf_expr:
            steps.append("\n2️⃣ Anwendung der Distributivität (DNF-Umformung):")
            steps.append("🔹 Regel: a * (b + c) = a * b + a * c")
            steps.append(f"🔹 Vorher: {expr}")
            steps.append(f"🔹 Nachher: {dnf_expr}")
        else:
            steps.append("\n2️⃣ Distributivität:")
            steps.append("🔹 Keine Umformung notwendig – bereits in DNF")

        # Schritt 2: Vereinfachung durch boolesche Gesetze
        simplified = simplify_logic(dnf_expr, form='dnf')
        if dnf_expr != simplified:
            steps.append("\n3️⃣ Weitere Vereinfachung:")
            steps.append("🔹 Gesetze: Idempotenz, Komplement, Absorption etc.")
            steps.append(f"🔹 Vorher: {dnf_expr}")
            steps.append(f"🔹 Nachher: {simplified}")
        else:
            steps.append("\n3️⃣ Weitere Vereinfachung:")
            steps.append("🔹 Keine weiteren Vereinfachungen möglich.")

        # Rückübersetzung für die Benutzeranzeige
        simplified_str = str(simplified).replace('|', '+').replace('&', '*').replace('~', '-')

        steps.append("\n✅ Endform (vereinfacht, DNF):")
        steps.append(f"🔹 {simplified_str}")

        # Ausgabe anzeigen
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "\n".join(steps))
        output_text.config(state='disabled')

    except Exception as e:
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"❌ Fehler: {str(e)}")
        output_text.config(state='disabled')

# GUI-Fenster
root = tk.Tk()
root.title("Boolescher Algebra-Rechner")
root.geometry("750x500")

# Eingabe
entry_label = tk.Label(root, text="Gib deinen Ausdruck ein (z. B. (a- b + c) * (a + b * c)):")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=80)
entry.pack(pady=5)

# Button
simplify_button = tk.Button(root, text="Vereinfachen", command=simplify_boolean)
simplify_button.pack(pady=10)

# Textausgabe mit schöner Schrift und automatischem Zeilenumbruch
output_text = tk.Text(
    root, height=22, width=95,
    wrap='word', font=('Courier New', 10),
    state='disabled', bg='lightyellow'
)
output_text.pack(pady=10)

# GUI starten
root.mainloop()
