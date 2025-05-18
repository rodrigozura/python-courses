import json

with open('curso_de_python/6.Lectura_y_escritortura_de_archivos/products.json', mode='r') as file:
    products = json.load(file)

for product in products:
    # print(product)
    print(f"Producto: {product['name']}, Precio: {product['price']}")