from collections import defaultdict

# defaultdict establece un valor por defecto
def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valor por defecto 0 
    product_count = defaultdict(int)
    print(product_count) # Output: {}
    for product in orders:
        # Agregamos una key del diccionario y un valor 1
        # Si la key ya existe, se suma 1 al valor existente
        product_count[product] +=1 
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)