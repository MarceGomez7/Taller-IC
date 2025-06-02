import tkinter as tk

# La lógica directamente en app.py
def mensaje():
    return "¡Hola, CI!"

def mostrar_mensaje():
    label.config(text=mensaje())

# Crear la ventana principal
root = tk.Tk()
root.title("Mi primera CI con GUI")

# Etiqueta inicial
label = tk.Label(root, text="¡Presiona el botón!")
label.pack(pady=10)

# Botón
boton = tk.Button(root, text="Saludar", command=mostrar_mensaje)
boton.pack(pady=10)

# Iniciar el loop principal
root.mainloop()
