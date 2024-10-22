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
   python3 editor_texto.py
2.Aparecerá una ventana con las siguientes opciones:
  . Abrir: Permite abrir un archivo de texto existente. El contenido del archivo se cargará en el área de texto.
  . Guardar: Guarda el contenido actual del área de texto en un nuevo archivo de texto o sobrescribe un archivo existente.

## Estructura del código
. EditorDeTexto: Clase principal que maneja la lógica del editor de texto.
  . abrir_archivo: Método que permite al usuario abrir un archivo de texto y cargar su contenido en el área de texto.
  . guardar_archivo: Método que permite al usuario guardar el contenido del área de texto en un archivo de texto.

## Contribuir
Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, siéntete libre de crear un pull request.
