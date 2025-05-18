# Read a file line by line
r"""
with open(r'D:\Curso de Python - Platzi\curso_de_python\6.Lectura_y_escritortura_de_archivos\cuento.txt', 'r') as file:
    for lines in file:
        print(lines.strip()) # Eliminar espacios en blanco al inicio y al final de cada línea
        #asi evitamos saltos de linea  innecesarios
"""


#Read a file the lines in a list
r"""
with open(r'D:\Curso de Python - Platzi\curso_de_python\6.Lectura_y_escritortura_de_archivos\cuento.txt', 'r') as file:
    lines = file.readlines()
    print(lines) # Imprime una lista con cada línea del archivo como un elemento de la lista

"""

# Add text
r"""
with open(r'D:\Curso de Python - Platzi\curso_de_python\6.Lectura_y_escritortura_de_archivos\cuento.txt', 'a') as file:
    file.write("\n\nBy: ChatGPT")
    
"""

#Sobreescribir un archivo
with open(r'D:\Curso de Python - Platzi\curso_de_python\6.Lectura_y_escritortura_de_archivos\cuento.txt', 'w') as file:
    file.write("Hello World")
