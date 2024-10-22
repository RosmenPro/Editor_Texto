"""4. Editor de Texto
Crea una interfaz gráfica de usuario (GUI) para simular nuestro propio editor de texto. Este
ejemplo también utiliza componentes estándar de GUI, incluyendo etiquetas, botones y
campos de entrada.
Puedes añadir la capacidad de abrir y guardar archivos, al igual que un editor de texto real."""
import tkinter as tk
from tkinter import filedialog

class EditorDeTexto:
    def __init__(self, master):
        self.master = master
        master.title("Editor de Texto")  # Establecemos el título de la ventana principal.

        # Creamos un widget de texto donde el usuario puede escribir.
        self.texto = tk.Text(master)
        self.texto.pack(expand=True, fill="both")  # Empaquetamos el widget de texto para que ocupe todo el espacio disponible.

        # Botón para abrir archivos.
        self.boton_abrir = tk.Button(master, text="Abrir", command=self.abrir_archivo)
        self.boton_abrir.pack(side=tk.LEFT)  # Empaquetamos el botón a la izquierda de la ventana.

        # Botón para guardar archivos.
        self.boton_guardar = tk.Button(master, text="Guardar", command=self.guardar_archivo)
        self.boton_guardar.pack(side=tk.LEFT)  # Empaquetamos el botón a la izquierda del botón "Abrir".

    def abrir_archivo(self):
        # Función para abrir un archivo de texto.
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if archivo:
            with open(archivo, "r") as f:
                contenido = f.read()
                self.texto.delete(1.0, tk.END)  # Borramos el contenido actual del área de texto.
                self.texto.insert(tk.END, contenido)  # Insertamos el contenido del archivo en el área de texto.

    def guardar_archivo(self):
        # Función para guardar el contenido del área de texto en un archivo.
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if archivo:
            with open(archivo, "w") as f:
                contenido = self.texto.get(1.0, tk.END)  # Obtenemos todo el texto del área de texto.
                f.write(contenido)  # Escribimos el contenido en el archivo.

root = tk.Tk()  # Creamos la ventana principal.
app = EditorDeTexto(root)  # Creamos una instancia de la clase EditorDeTexto.
root.mainloop()  # Iniciamos el bucle principal de la interfaz gráfica.