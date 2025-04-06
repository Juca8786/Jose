# Autor: José Luis
# Fecha: Abril 2025
# Tarea: Trabajo con archivos de texto en Python

# Primera parte: Escritura en el archivo

# Abro (o creo si no existe) un archivo de texto llamado 'my_notes.txt' en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribo tres notas personales. Estas notas pueden ser ideas o recordatorios.
archivo.write("Hoy aprendí a escribir archivos con Python.\n")
archivo.write("Es importante cerrar los archivos después de usarlos.\n")
archivo.write("También debo practicar más para dominar el tema.\n")

# Cierro el archivo después de escribir, para guardar los cambios y liberar recursos
archivo.close()

# Segunda parte: Lectura del archivo

# Ahora abro el archivo en modo lectura ('r') para leer lo que escribí antes
archivo = open("my_notes.txt", "r")

# Leo línea por línea y las muestro en la consola
print("Leyendo el contenido del archivo my_notes.txt:\n")

linea = archivo.readline()  # Leo la primera línea

# Uso un bucle while para seguir leyendo mientras haya texto
while linea != "":
    print(linea.strip())  # .strip() elimina los saltos de línea al final
    linea = archivo.readline()  # Leo la siguiente línea

# Finalmente, cierro el archivo después de leer
archivo.close()
