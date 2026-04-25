# programa python en repositorio mejorado
import tkinter as tk

ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("400x250")
ventana.config(bg="#1e1e2f")

etiqueta = tk.Label(
    ventana,
    text="Este programa es de axel y samuel",
    font=("Helvetica", 16, "bold"),
    fg="red",
    bg="#1e1e2f"
)

# Centrado real en la ventana
etiqueta.pack(expand=True)

ventana.mainloop()