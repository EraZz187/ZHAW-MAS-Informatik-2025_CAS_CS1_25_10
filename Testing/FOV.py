import tkinter as tk
from tkinter import ttk
import math

def calculate_fov():
    try:
        # Eingabewerte holen
        sensor_width = float(entry_sensor_width.get())
        sensor_height = float(entry_sensor_height.get())
        focal_length = float(entry_focal_length.get())
        distance = float(entry_distance.get())

        # Diagonale & FOV in Grad
        diagonal = math.sqrt(sensor_width ** 2 + sensor_height ** 2)
        fov_h = 2 * math.degrees(math.atan(sensor_width / (2 * focal_length)))
        fov_v = 2 * math.degrees(math.atan(sensor_height / (2 * focal_length)))
        fov_d = 2 * math.degrees(math.atan(diagonal / (2 * focal_length)))

        # Sichtfeld in Metern (X und Y)
        view_x = 2 * distance * math.tan(math.radians(fov_h / 2))
        view_y = 2 * distance * math.tan(math.radians(fov_v / 2))

        result_var.set(
            f"📐 FOV (in Grad):\n"
            f"Horizontal: {fov_h:.2f}°\n"
            f"Vertikal:   {fov_v:.2f}°\n"
            f"Diagonal:   {fov_d:.2f}°\n\n"
            f"📏 Sichtfeld bei {distance} m Abstand:\n"
            f"X (horizontal): {view_x:.2f} m\n"
            f"Y (vertikal):   {view_y:.2f} m"
        )

    except ValueError:
        result_var.set("❌ Bitte gültige Zahlen eingeben.")

# GUI erstellen
root = tk.Tk()
root.title("FOV-Rechner (mit X/Y-Sichtfeld)")
root.geometry("360x420")
root.resizable(False, False)

# Eingabefelder
ttk.Label(root, text="Sensorbreite (mm):").pack(pady=(10, 0))
entry_sensor_width = ttk.Entry(root)
entry_sensor_width.pack()

ttk.Label(root, text="Sensorhöhe (mm):").pack(pady=(10, 0))
entry_sensor_height = ttk.Entry(root)
entry_sensor_height.pack()

ttk.Label(root, text="Brennweite (mm):").pack(pady=(10, 0))
entry_focal_length = ttk.Entry(root)
entry_focal_length.pack()

ttk.Label(root, text="Arbeitsabstand (m):").pack(pady=(10, 0))
entry_distance = ttk.Entry(root)
entry_distance.pack()

# Button
ttk.Button(root, text="Berechnen", command=calculate_fov).pack(pady=15)

# Ausgabe
result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var, justify="left", font=("Courier", 10)).pack(padx=10)

root.mainloop()
