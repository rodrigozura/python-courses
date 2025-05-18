my_list = [1, 2, 3, 4, 5]

# Iteradores
it = iter(my_list)
print(next(it))  # next() devuelve el siguiente elemento del iterador
print(next(it))  # next() devuelve el siguiente elemento del iterador
print(next(it))  # next() devuelve el siguiente elemento del iterador
print(next(it))  # next() devuelve el siguiente elemento del iterador
print(next(it))  # next() devuelve el siguiente elemento del iterador
# print(next(it))  # aqui falla porque no hay mas elementos

print("-------------")
# Itaradores cadenas
texto = "Hola Mundo"

# Creando objeto iterador
iter_texto = iter(texto)

# iterar en la cadena
for char in iter_texto:
    print(char)



print("-------------")
# Iterador impares
# Limite
limit = 10
# Crear objeto iterador
odd_itter = iter(range(1, limit + 1))

# Usar iterador
for num in odd_itter:
    if num % 2 == 0:
        continue
    print(num)

print("-------------")
# Generadores
def my_generator():
    yield 1
    yield 2
    yield 3

"""
yield es una palabra clave en Python utilizada en funciones generadoras. 
A diferencia de return, que finaliza la función y devuelve un valor, yield 
permite pausar la función y devolver un valor al llamador, manteniendo su 
estado para continuar la ejecución en el futuro. Esto es útil para crear 
iteradores que pueden producir una secuencia de valores sin mantener toda 
la información en memoria, optimizando así el uso de recursos. Esencialmente, 
yield permite manejar grandes conjuntos de datos de forma eficiente y eficaz.
"""
for value in my_generator():
    print(value)

print("------------- Fibonacci")
# Fibonacci
def fibonacci(limit):
    a, b = 0, 1 # otra manera de definir a y b en una sola linea
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)