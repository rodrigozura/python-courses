x = 5

def modify_global():
    global x
    x += 3
    print(f'El valor de la variable global dentro de la función es: {x}')

modify_global()
print(f'El valor de la variable global después de la función: {x}')