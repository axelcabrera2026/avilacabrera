import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime

# -------------------------
# LISTAS PARA GUARDAR DATOS
# -------------------------
productos = []
ventas = []

# -------------------------
# FUNCIONES PRODUCTOS
# -------------------------
def abrir_registro_productos():

    ventana_productos = tk.Toplevel()
    ventana_productos.title("Registro de Productos")
    ventana_productos.geometry("400x400")
    ventana_productos.configure(bg="#dbe9f4")

    tk.Label(ventana_productos, text="Nombre del Producto",
             bg="#dbe9f4", font=("Arial", 12)).pack(pady=5)

    entry_nombre = tk.Entry(ventana_productos, width=30)
    entry_nombre.pack()

    tk.Label(ventana_productos, text="Precio",
             bg="#dbe9f4", font=("Arial", 12)).pack(pady=5)

    entry_precio = tk.Entry(ventana_productos, width=30)
    entry_precio.pack()

    tk.Label(ventana_productos, text="Cantidad",
             bg="#dbe9f4", font=("Arial", 12)).pack(pady=5)

    entry_cantidad = tk.Entry(ventana_productos, width=30)
    entry_cantidad.pack()

    lista_productos = tk.Listbox(ventana_productos, width=50)
    lista_productos.pack(pady=15)

    def guardar_producto():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()

        if nombre == "" or precio == "" or cantidad == "":
            messagebox.showerror("Error", "Completa todos los campos")
            return

        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

        lista_productos.insert(
            tk.END,
            f"{nombre} - ${precio} - Stock: {cantidad}"
        )

        messagebox.showinfo("Éxito", "Producto guardado")

        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)

    tk.Button(
        ventana_productos,
        text="Guardar Producto",
        bg="#1f6aa5",
        fg="white",
        command=guardar_producto
    ).pack(pady=10)


# -------------------------
# FUNCIONES VENTAS
# -------------------------
def abrir_registro_ventas():

    ventana_ventas = tk.Toplevel()
    ventana_ventas.title("Registro de Ventas")
    ventana_ventas.geometry("450x450")
    ventana_ventas.configure(bg="#dbe9f4")

    tk.Label(
        ventana_ventas,
        text="Selecciona Producto",
        bg="#dbe9f4",
        font=("Arial", 12)
    ).pack(pady=5)

    combo_productos = ttk.Combobox(
        ventana_ventas,
        values=[p["nombre"] for p in productos],
        width=30
    )
    combo_productos.pack()

    tk.Label(
        ventana_ventas,
        text="Cantidad",
        bg="#dbe9f4",
        font=("Arial", 12)
    ).pack(pady=5)

    entry_cantidad = tk.Entry(ventana_ventas, width=30)
    entry_cantidad.pack()

    lista_ventas = tk.Listbox(ventana_ventas, width=55)
    lista_ventas.pack(pady=15)

    def realizar_venta():

        producto_nombre = combo_productos.get()
        cantidad = entry_cantidad.get()

        if producto_nombre == "" or cantidad == "":
            messagebox.showerror("Error", "Completa los campos")
            return

        cantidad = int(cantidad)

        for producto in productos:

            if producto["nombre"] == producto_nombre:

                if producto["cantidad"] >= cantidad:

                    total = producto["precio"] * cantidad
                    producto["cantidad"] -= cantidad

                    venta = {
                        "producto": producto_nombre,
                        "cantidad": cantidad,
                        "total": total,
                        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
                    }

                    ventas.append(venta)

                    lista_ventas.insert(
                        tk.END,
                        f"{producto_nombre} | Cantidad: {cantidad} | Total: ${total}"
                    )

                    messagebox.showinfo(
                        "Venta realizada",
                        f"Total a pagar: ${total}"
                    )

                else:
                    messagebox.showerror(
                        "Error",
                        "No hay suficiente stock"
                    )

    tk.Button(
        ventana_ventas,
        text="Realizar Venta",
        bg="#1f6aa5",
        fg="white",
        command=realizar_venta
    ).pack(pady=10)


# -------------------------
# FUNCIONES REPORTES
# -------------------------
def abrir_reportes():

    ventana_reportes = tk.Toplevel()
    ventana_reportes.title("Reportes")
    ventana_reportes.geometry("500x500")
    ventana_reportes.configure(bg="#dbe9f4")

    texto = tk.Text(ventana_reportes, width=60, height=25)
    texto.pack(pady=15)

    texto.insert(tk.END, "========= REPORTE DE VENTAS =========\n\n")

    total_general = 0

    for venta in ventas:

        texto.insert(
            tk.END,
            f"Producto: {venta['producto']}\n"
        )

        texto.insert(
            tk.END,
            f"Cantidad: {venta['cantidad']}\n"
        )

        texto.insert(
            tk.END,
            f"Total: ${venta['total']}\n"
        )

        texto.insert(
            tk.END,
            f"Fecha: {venta['fecha']}\n"
        )

        texto.insert(
            tk.END,
            "-----------------------------\n"
        )

        total_general += venta["total"]

    texto.insert(
        tk.END,
        f"\nTOTAL GENERAL VENDIDO: ${total_general}"
    )


# -------------------------
# ACERCA DE
# -------------------------
def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Punto de Venta de Ropa\n"
        "Proyecto Escolar\n"
        "Versión 1.0"
    )


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - Tienda de Ropa")
ventana.geometry("500x650")
ventana.resizable(False, False)
ventana.configure(bg="#09294e")

# -------------------------
# ESTILO BOTONES
# -------------------------
estilo = ttk.Style()
estilo.theme_use("default")

estilo.configure(
    "Custom.TButton",
    font=("Arial", 12, "bold"),
    padding=10,
    foreground="white",
    background="#1f6aa5"
)

estilo.map(
    "Custom.TButton",
    background=[("active", "#144d7a")]
)

# -------------------------
# LOGO
# -------------------------
try:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((220, 220))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg="#09294e"
    )

    lbl_logo.pack(pady=20)

except:

    lbl_sin_logo = tk.Label(
        ventana,
        text="(Aquí va el logo)",
        font=("Arial", 16),
        fg="white",
        bg="#09294e"
    )

    lbl_sin_logo.pack(pady=40)

# -------------------------
# TITULO
# -------------------------
titulo = tk.Label(
    ventana,
    text="SISTEMA PUNTO DE VENTA",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#09294e"
)

titulo.pack(pady=10)

# -------------------------
# BOTONES
# -------------------------
btn_reg_prod = ttk.Button(
    ventana,
    text="Registro de Productos",
    style="Custom.TButton",
    command=abrir_registro_productos
)

btn_reg_prod.pack(pady=15, ipadx=10)

btn_reg_ventas = ttk.Button(
    ventana,
    text="Registro de Ventas",
    style="Custom.TButton",
    command=abrir_registro_ventas
)

btn_reg_ventas.pack(pady=15, ipadx=10)

btn_reportes = ttk.Button(
    ventana,
    text="Reporte de Ventas",
    style="Custom.TButton",
    command=abrir_reportes
)

btn_reportes.pack(pady=15, ipadx=10)

btn_acerca = ttk.Button(
    ventana,
    text="Acerca de",
    style="Custom.TButton",
    command=abrir_acerca_de
)

btn_acerca.pack(pady=15, ipadx=10)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()