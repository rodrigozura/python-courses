# **kwargs es una variable que toma todos los argumentos que se le pasen a la funcion
# las particularidades de kwargs es que se le pasan como un diccionario
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='Carlos', age=30, city='Bogotá')
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia')