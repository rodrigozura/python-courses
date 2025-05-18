import csv

new_product = {
    'name': 'Placa de video',
    'price': 200,
    'quantity': 10,
    'brand': 'NVIDIA',
    'category': 'Hardware',
    'entry_date': '2023-10-01',
}

with open('curso_de_python/6.Lectura_y_escritortura_de_archivos/products.csv', mode='a', newline='') as archivo_csv:
    archivo_csv.write('\n')
    csv_writer = csv.DictWriter(archivo_csv, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)