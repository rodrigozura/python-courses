x = 'global'

# Funcion exxterna
def outer_function():
    x = 'enclosing'

    # Funcion interna
    def inner_function():
        x = 'local'
        print(f'Valor de x en la funcion interna: {x}')

    inner_function()
    print(f'Valor de x en la funcion exterior: {x}')

outer_function()
print(f'Valor de x en el ámbito global: {x}')