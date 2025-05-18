
def check_access(func):
    def wrapper(employee):
        # Comprobar si el empleado tiene acceso
        if employee.get('role') == 'admin':
            print('Acceso concedido')
            return func(employee)
        else:
            print('Acceso denegado')
    return wrapper

@check_access
def delete_employee(employee):
    print(f'Empleado {employee['name']} ha sido eliminado')

employee_1 = {'name': 'Juan', 'role': 'admin'}
employee_2 = {'name': 'Maria', 'role': 'user'}
delete_employee(employee_1)  # Acceso concedido
delete_employee(employee_2)  # Acceso denegado