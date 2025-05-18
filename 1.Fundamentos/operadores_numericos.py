# Operadores numericos
a = 10
b = 3
print(a + b) # Suma
print(a - b) # Resta
print(a * b) # Multiplicacion
print(a / b) # Division
print(a // b) # Division entera
print(a % b) # Resto de la división
print(a ** b) # Potencia
print(a ** 2) # Potencia al cuadrado
print(a ** 0.5) # Potencia al cuadrado
print(a ** -1) # Potencia al cuadrado

# Operadores de asignación
a = 10
b = 3
a += b # Suma y asigna
a -= b # Resta y asigna
a *= b # Multiplicacion y asigna
a /= b # Division y asigna
a //= b # Division entera y asigna
a %= b # Resto de la división y asigna
a **= b # Potencia y asigna

# Operadores de comparación
a = 10
b = 3
print(a == b) # Igual
print(a != b) # Diferente
print(a > b) # Mayor que
print(a < b) # Menor que
print(a >= b) # Mayor o igual que
print(a <= b) # Menor o igual que

# Operadores de lógica
a = True
b = False
print(a and b) # Y
print(a or b) # O
print(not a) # No   

c = 2
#  Regla Pemda (Order of operations)
#  Que es pemda? Pemda es la regla de orden de operaciones que se sigue en la computación
#  Cuando se realiza una operación, se sigue el orden de operaciones que se indica en la regla de peda
#  Primero se realizan las operaciones dentro de los paréntesis, luego las multiplicaciones y divisiones, y por último las sumas y restas.
#  Por ejemplo, si se realiza la operación a + b * c, se realizará la siguiente secuencia de operaciones:
#  a + (b * c)
print(a + b * c) # Suma
print(a + (b * c)) # Suma
print(a + b + c) # Suma
print(a + b - c) # Suma
print(a - b + c) # Suma
print(a - b - c) # Suma
print(a * b + c) # Suma
print(a * b - c) # Suma
print(a + b / c) # Suma
print(a + b // c) # Suma
print(a + b % c) # Suma
