import math
from collections import Counter


def berechne_entropie_text(text):
    frequenzen = Counter(text)
    gesamt = len(text)
    entropie = -sum((freq / gesamt) * math.log2(freq / gesamt) for freq in frequenzen.values())
    return entropie


def berechne_entropie_wahrscheinlichkeiten(p_liste):
    return -sum(p * math.log2(p) for p in p_liste if p > 0)


def main():
    print("=== Entropie-Rechner ===")
    modus = input("Modus wählen: (1) Text-Eingabe oder (2) Wahrscheinlichkeiten? ")

    if modus == "1":
        text = input("Bitte Text eingeben: ")
        entropie = berechne_entropie_text(text)
        print(f"Entropie des Textes: {entropie:.4f} Bits/Symbol")

    elif modus == "2":
        p_input = input("Wahrscheinlichkeiten (durch Komma getrennt, z. B. 0.2,0.3,0.5): ")
        try:
            p_liste = [float(p.strip()) for p in p_input.split(",")]
            if abs(sum(p_liste) - 1.0) > 0.01:
                print("⚠️ Hinweis: Die Summe der Wahrscheinlichkeiten ist nicht gleich 1.")
            entropie = berechne_entropie_wahrscheinlichkeiten(p_liste)
            print(f"Entropie der Verteilung: {entropie:.4f} Bits/Symbol")
        except ValueError:
            print("❌ Ungültige Eingabe.")

    else:
        print("❌ Ungültiger Modus gewählt.")


if __name__ == "__main__":
    main()