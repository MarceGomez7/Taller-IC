import tkinter as tk
from PIL import Image, ImageTk
from logic import mensaje  # ✅ Importa desde logic.py

def mostrar_mensaje():
    label.config(text=mensaje())
    mostrar_logo()

def mostrar_logo():
    imagen = Image.open("../img/utn.png")
    imagen = imagen.resize((300, 300), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen)

    logo_label.config(image=imagen_tk)
    logo_label.image = imagen_tk

root = tk.Tk()
root.title("Integracion Continua 2025")
root.geometry("400x400")
root.configure(bg="#1e1e2f")

label = tk.Label(
    root,
    text="¡Presiona el botón!",
    font=("Helvetica", 18, "bold"),
    fg="#ffffff",
    bg="#1e1e2f"
)
label.pack(pady=20)

boton = tk.Button(
    root,
    text="💥 Saludar 💥",
    command=mostrar_mensaje,
    font=("Helvetica", 14, "bold"),
    bg="#06083d",
    fg="#ffffff",
    activebackground="#10007B",
    activeforeground="#1e1e2f",
    padx=20,
    pady=10,
    bd=0,
    relief="raised",
    cursor="hand2"
)
boton.pack(pady=10)

logo_label = tk.Label(root, bg="#1e1e2f")
logo_label.pack(pady=10)

root.mainloop()
