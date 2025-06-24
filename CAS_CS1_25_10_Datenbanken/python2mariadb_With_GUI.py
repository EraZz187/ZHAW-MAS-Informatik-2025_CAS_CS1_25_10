import tkinter as tk
from tkinter import messagebox
import mariadb

# Verbindung aufbauen
try:
    conn = mariadb.connect(
        user="pythonAppUser",
        password="-w-3-b-007-c0n",
        host="localhost",
        port=3306,
        database="cas cs1 fs25"  # Leerzeichen vermeiden!
    )
    cur = conn.cursor()
except mariadb.Error as e:
    messagebox.showerror("Verbindungsfehler", f"Fehler beim Verbinden mit der Datenbank:\n{e}")
    exit()

# Funktionen
def add_data():
    try:
        cur.execute(
            "INSERT INTO mitarbeiter (manummer, vorname, nachname, abtnummer) VALUES (?, ?, ?, ?)",
            (entry_id.get(), entry_vorname.get(), entry_nachname.get(), entry_abt.get())
        )
        conn.commit()
        messagebox.showinfo("Erfolg", "Eintrag erfolgreich hinzugefügt.")
    except mariadb.Error as e:
        messagebox.showerror("Fehler", f"Fehler beim Einfügen:\n{e}")

def search_data():
    try:
        result_text.delete("1.0", tk.END)
        cur.execute("SELECT manummer, vorname, nachname FROM mitarbeiter WHERE nachname LIKE ?",
                    ("%" + entry_suche.get() + "%",))
        for (ma_num, vorname, nachname) in cur:
            result_text.insert(tk.END, f"{ma_num} | {vorname} {nachname}\n")
    except mariadb.Error as e:
        messagebox.showerror("Fehler", f"Fehler bei der Suche:\n{e}")

def get_same_dept():
    try:
        result_text.delete("1.0", tk.END)
        cur.callproc('getmaderselbenabteilung', [entry_suche_id.get()])
        for (ma_num, vorname, nachname) in cur:
            result_text.insert(tk.END, f"{ma_num} | {vorname} {nachname}\n")
    except mariadb.Error as e:
        messagebox.showerror("Fehler", f"Fehler beim Abrufen der Abteilung:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Mitarbeiterverwaltung")
root.geometry("600x500")

# Eingabefelder
tk.Label(root, text="Mitarbeiter ID:").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Vorname:").pack()
entry_vorname = tk.Entry(root)
entry_vorname.pack()

tk.Label(root, text="Nachname:").pack()
entry_nachname = tk.Entry(root)
entry_nachname.pack()

tk.Label(root, text="Abteilungsnummer:").pack()
entry_abt = tk.Entry(root)
entry_abt.pack()

tk.Button(root, text="Einfügen", command=add_data).pack(pady=5)

tk.Label(root, text="Nachname suchen:").pack()
entry_suche = tk.Entry(root)
entry_suche.pack()

tk.Button(root, text="Suchen", command=search_data).pack(pady=5)

tk.Label(root, text="ID für gleiche Abteilung:").pack()
entry_suche_id = tk.Entry(root)
entry_suche_id.pack()

tk.Button(root, text="Abteilungs-Kollegen anzeigen", command=get_same_dept).pack(pady=5)

# Ergebnisbereich
tk.Label(root, text="Ergebnisse:").pack()
result_text = tk.Text(root, height=10, width=60)
result_text.pack()

# Fenster schließen und aufräumen
def on_closing():
    cur.close()
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
