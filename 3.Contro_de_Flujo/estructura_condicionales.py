x = 10
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")

x = 15
y = 20
# Operadores lógicos
if x > 10 and y > 10:
    print("x y son mayores que 10")
elif x > 10 or y > 10:
    print("x o y son mayores que 10")
elif not (x > 10 and y > 10):
    print("x y no son mayores que 10")
else:
    print("x y son menores que 10")

# Operadores de comparación
a = 10
b = 3
if a == b:
    print("a es igual a b")
elif a != b:
    print("a es diferente a b")
elif a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
elif a >= b:
    print("a es mayor o igual que b")
elif a <= b:
    print("a es menor o igual que b")

# Operadores de identidad
a = 10
b = 3
if a is b:
    print("a es igual a b")
elif a is not b:
    print("a es diferente a b")

# Operadores de booleanos
a = True
b = False
if a and b:
    print("a y b son verdaderos")
elif a or b:
    print("a o b son verdaderos")
else:
    print("a y b son falsos")