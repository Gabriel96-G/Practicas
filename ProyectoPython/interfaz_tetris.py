import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess

# --- Función que ejecuta tu código original ---
def ejecutar_programa():
    salida_text.delete(1.0, tk.END)  # Limpia el área de texto
    
    apilamiento = entry_apilamiento.get()
    lineas = entry_lineas.get()
    pieza = entry_pieza.get()

    # Construimos las entradas que tu código espera (en orden)
    entrada = f"{apilamiento}\n{lineas}\n{pieza}\n"

    # Ejecutamos tu archivo original sin modificarlo
    proceso = subprocess.run(
        ["python", "original_tetris.py"],
        input=entrada,
        text=True,
        capture_output=True
    )

    # Mostramos la salida del programa
    salida_text.insert(tk.END, proceso.stdout)
    if proceso.stderr:
        salida_text.insert(tk.END, "\n--- ERRORES ---\n" + proceso.stderr)

# --- Interfaz gráfica ---
root = tk.Tk()
root.title("Interfaz Tetris - Programación Estructurada")
root.geometry("540x500")
root.config(bg="#E3F2FD")

tk.Label(root, text="Simulación de Tetris", font=("Arial", 16, "bold"), bg="#E3F2FD", fg="#0D47A1").pack(pady=10)

frame = tk.Frame(root, bg="#E3F2FD")
frame.pack(pady=10)

tk.Label(frame, text="Apilamiento:", bg="#E3F2FD", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)
entry_apilamiento = tk.Entry(frame, width=10)
entry_apilamiento.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Cantidad de líneas:", bg="#E3F2FD", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5)
entry_lineas = tk.Entry(frame, width=10)
entry_lineas.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Pieza (o,l,s,z,L,J,T):", bg="#E3F2FD", font=("Arial", 11)).grid(row=2, column=0, padx=5, pady=5)
entry_pieza = tk.Entry(frame, width=10)
entry_pieza.grid(row=2, column=1, padx=5, pady=5)

boton = tk.Button(root, text="Ejecutar código original", command=ejecutar_programa, bg="#1976D2", fg="white", font=("Arial", 11, "bold"))
boton.pack(pady=10)

salida_text = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD, font=("Courier", 10))
salida_text.pack(padx=10, pady=10)

root.mainloop()
