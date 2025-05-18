import csv

# Leer archivo cvs
r"""with open('curso_de_python/6.Lectura_y_escritortura_de_archivos/products.csv', mode='r') as archivo_csv:
    csv_reader = csv.DictReader(archivo_csv)
    for row in csv_reader:
        print(row)

"""

# Mostrar la informacion por columnas
with open('curso_de_python/6.Lectura_y_escritortura_de_archivos/products.csv', mode='r') as archivo_csv:
    csv_reader = csv.DictReader(archivo_csv)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")