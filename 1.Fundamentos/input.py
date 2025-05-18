name = input("¿Cuál es tu nombre? ")
print("Hola " + name)

age = input("¿Cuál es tu edad? ")
print("Tu edad es " + age)

# Siempre que ingresamos un valor por teclado, este se guarda como un string
# Por lo tanto tenemos que hacer un artificio llamado casting
age = int(age)

if age >= 18:
    print("¡Bienvenido!")
else:
    print("¡Eres menor de edad!")