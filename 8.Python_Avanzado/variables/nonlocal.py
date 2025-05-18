def outer_function():
    x = 'enclosing'
    def inner_function():
        nonlocal x
        x = 'modified'
        print(f'Valor de x en la funcion interna: {x}')
    inner_function()
    print(f'Valor de x en la funcion exterior: {x}')

outer_function()