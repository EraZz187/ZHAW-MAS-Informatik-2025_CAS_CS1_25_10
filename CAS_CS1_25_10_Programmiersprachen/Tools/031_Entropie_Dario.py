import tkinter as tk
from tkinter import messagebox
import math
from collections import Counter


def berechne_entropie_und_vergleiche():
    # Eingabe Wahrscheinlichkeiten
    eingabe = eingabe_box.get("1.0", tk.END).strip()
    alphabet_probs = {}
    for zeile in eingabe.splitlines():
        teile = zeile.strip().split()
        if len(teile) != 2:
            continue
        zeichen, wahrsch = teile
        try:
            p = float(wahrsch.replace(",", "."))
            if len(zeichen) != 1 or not (0 < p <= 1):
                continue
            alphabet_probs[zeichen] = p
        except:
            continue

    if not alphabet_probs:
        messagebox.showerror("Fehler", "Ungültige Eingabe für Wahrscheinlichkeiten.")
        return

    # Ursprüngliche Entropie
    ursprüngliche_entropie = -sum(p * math.log2(p) for p in alphabet_probs.values())

    # GUI-Ausgabe vorbereiten
    result_box.config(state='normal')
    result_box.delete("1.0", tk.END)

    result_box.insert(tk.END, "📌 Ursprüngliche Wahrscheinlichkeiten:\n")
    for z, p in alphabet_probs.items():
        result_box.insert(tk.END, f"{z!r}: {p:.3f}\n")

    # Informationsgehalt je Zeichen
    result_box.insert(tk.END, "\nℹ️ Informationsgehalt je Zeichen:\n")
    for z, p in alphabet_probs.items():
        info = math.log2(1 / p)
        result_box.insert(tk.END, f"I({z!r}) = log2(1/{p}) = {info:.3f} Bit\n")

    result_box.insert(tk.END, f"\n🧠 Ursprüngliche Entropie: {ursprüngliche_entropie:.4f} Bit/Z\n")

    # Optional: Textbasierte Entropie
    text = text_box.get("1.0", tk.END).strip()
    text = ''.join(text.split())

    if text:
        text_counter = Counter(text)
        gesamt = sum(text_counter[zeichen] for zeichen in alphabet_probs.keys())

        if gesamt > 0:
            text_probs = {z: text_counter[z] / gesamt for z in alphabet_probs if text_counter[z] > 0}
            neue_entropie = -sum(p * math.log2(p) for p in text_probs.values())

            result_box.insert(tk.END, "\n📝 Verteilung im Text:\n")
            for z, p in text_probs.items():
                result_box.insert(tk.END, f"{z!r}: {p:.3f}\n")

            result_box.insert(tk.END, f"\n🧮 Entropie basierend auf dem Text: {neue_entropie:.4f} Bit/Z\n")
        else:
            result_box.insert(tk.END, "\n⚠️ Hinweis: Keine gültigen Zeichen aus dem Alphabet im Text gefunden.\n")

    result_box.config(state='disabled')


# GUI Setup
root = tk.Tk()
root.title("Entropieberechner mit Informationsgehalt")

# Eingabe Wahrscheinlichkeiten
tk.Label(root, text="Wahrscheinlichkeiten eingeben (z. B. e 0.5)").pack()
eingabe_box = tk.Text(root, width=30, height=6, font=("Courier", 12))
eingabe_box.pack(pady=5)

# Optionaler Text
tk.Label(root, text="Optionaler Text (nur Zeichen aus dem Alphabet):").pack()
text_box = tk.Text(root, width=40, height=4, font=("Courier", 12))
text_box.pack(pady=5)

# Button
tk.Button(root, text="Berechnen", command=berechne_entropie_und_vergleiche).pack(pady=10)

# Ergebnisanzeige
result_box = tk.Text(root, width=60, height=25, font=("Courier", 11), state='disabled')
result_box.pack(pady=5)

root.mainloop()