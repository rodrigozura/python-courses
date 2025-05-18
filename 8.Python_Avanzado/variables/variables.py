x = 100

def local_function():
    x = 10
    print(f'El valor de la variable local es: {x}')

def show_global():
    print(f'El valor de la variable global es: {x}')

local_function()
# print(x) # Esto generará un error porque x no está definida en el ámbito global

show_global()
print(x) # Esto mostrará el valor de la variable global
