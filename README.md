
# Editor de Texto

Este es un editor de texto simple desarrollado en Python utilizando la biblioteca `tkinter`. Permite a los usuarios escribir texto, así como abrir y guardar archivos de texto, emulando las funciones básicas de un editor de texto real.

## Funcionalidades

- Interfaz gráfica de usuario (GUI) para una experiencia amigable.
- Permite escribir texto en un área de trabajo.
- Opción para abrir archivos de texto existentes.
- Opción para guardar el contenido del editor en un archivo de texto.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.x
- Tkinter (generalmente incluido en las instalaciones estándar de Python)

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener `tkinter` instalado. Si no lo tienes, puedes instalarlo ejecutando:

   ```bash
   sudo apt-get install python3-tk  # En sistemas basados en Debian/Ubuntu
   ```

## Uso

1. Ejecuta el script:
   ```bash
   python3 editor_texto.py
   ```

2. Aparecerá una ventana con las siguientes opciones:
   * Abrir: Permite abrir un archivo de texto existente. El contenido del archivo se cargará en el área de texto.
   * Guardar: Guarda el contenido actual del área de texto en un nuevo archivo de texto o sobrescribe un archivo existente.

## Estructura del código

* EditorDeTexto: Clase principal que maneja la lógica del editor de texto.
  * abrir_archivo: Método que permite al usuario abrir un archivo de texto y cargar su contenido en el área de texto.
  * guardar_archivo: Método que permite al usuario guardar el contenido del área de texto en un archivo de texto.

## Contribuir

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, siéntete libre de crear un pull request.

---

# Text Editor

This is a simple text editor developed in Python using the `tkinter` library. It allows users to write text, as well as open and save text files, emulating the basic functions of a real text editor.

## Features

- Graphical User Interface (GUI) for a user-friendly experience.
- Allows typing text in a workspace area.
- Option to open existing text files.
- Option to save the editor's content to a text file.

## Requirements

To run this project, you need to have installed:

- Python 3.x
- Tkinter (usually included in standard Python installations)

## Installation

1. Clone this repository or download the files.
2. Ensure `tkinter` is installed. If not, you can install it by running:

   ```bash
   sudo apt-get install python3-tk  # On Debian/Ubuntu-based systems
   ```

## Usage

1. Run the script:
   ```bash
   python3 editor_texto.py
   ```

2. A window with the following options will appear:
   * Open: Allows you to open an existing text file. The file's content will be loaded into the text area.
   * Save: Saves the current content of the text area to a new text file or overwrites an existing file.

## Code Structure

* `EditorDeTexto`: Main class that handles the logic of the text editor.
  * `abrir_archivo`: Method that allows the user to open a text file and load its content into the text area.
  * `guardar_archivo`: Method that allows the user to save the content of the text area to a text file.

## Contributing

Contributions are welcome. If you have any suggestions or improvements, feel free to create a pull request.
