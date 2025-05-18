import csv

file_path = 'curso_de_python/6.Lectura_y_escritortura_de_archivos/products.csv'
updated_file_path = 'curso_de_python/6.Lectura_y_escritortura_de_archivos/products_updated2.csv'

with open(file_path, mode='r') as archivo_csv:
    csv_reader = csv.DictReader(archivo_csv)
    # Obtener los nombres de las columnas existentes
    column_names = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=column_names)
        csv_writer.writeheader()

        for row in csv_reader:
            # Calcular el precio total
            total_value = float(row['price']) * int(row['quantity'])
            # Agregar la nueva columna al diccionario
            row['total_value'] = total_value
            # Escribir la fila actualizada en el nuevo archivo
            csv_writer.writerow(row)