import tkinter as tk
from PIL import Image, ImageTk 

# Lógica del mensaje
def mensaje():
    return "¡Hola, clickeaste en el Botón!"

def mostrar_mensaje():
    label.config(text=mensaje())
    mostrar_logo()

def mostrar_logo():
    # Abrir la imagen y redimensionarla
    imagen = Image.open("../img/utn.png")
    imagen = imagen.resize((300, 300), Image.Resampling.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen)
    
    # Asignar la imagen a la etiqueta de la imagen
    logo_label.config(image=imagen_tk)
    logo_label.image = imagen_tk  # Necesario para evitar que se pierda la referencia

# Crear la ventana principal
root = tk.Tk()
root.title("Integracion Continua 2025")

# Colores y estilo
root.geometry("400x400")
root.configure(bg="#1e1e2f")  # Fondo oscuro

# Etiqueta inicial
label = tk.Label(
    root,
    text="¡Presiona el botón!",
    font=("Helvetica", 18, "bold"),
    fg="#ffffff",
    bg="#1e1e2f"
)
label.pack(pady=20)

# Botón con estilo
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

# Etiqueta para mostrar el logo
logo_label = tk.Label(root, bg="#1e1e2f")
logo_label.pack(pady=10)

# Iniciar el loop principal
root.mainloop()
