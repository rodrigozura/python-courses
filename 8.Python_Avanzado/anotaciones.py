# IDs de empleados
id1: int = 101
id2: int = 102

# Sumar los IDs


def add_ids(id1: int, id2: int) -> int:
    """
    Suma los IDs de empleados

    :param id1 (int): ID del primer empleado
    :param id2 (int): ID del segundo empleado

    Retorna:
    int: La suma de los IDs
    """
    total_id: int = id1 + id2
    return total_id

class Employee:
    name: str
    age: int
    salary: float
    
    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str: # Aca podemos ver como indicamos el retorno de la funcion
        return f'Hola, soy {self.name}, tengo {self.age} años y mi salario es {self.salary} USD al mes.'
    
# Crear una instancia de la clase Employee
employee = Employee('Juan', 28, 3500)
print(employee.introduce())

from typing import Optional

# Aqui con optional el id encontrado puede ser un int o None

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.
    employee_id (int): ID a buscar.

    Retorna:
    Optional[int]: El ID encontrado o None si no existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None

from typing import Union

# Union permite indicar que el salario puede ser un int o float
# En este caso, el salario se convierte a float independientemente de su tipo original

def process_salary(salary: Union[int, float]) -> float:
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)


# Tipos comunes en anotaciones
"""
int: Entero
float: Número de punto flotante
str: Cadena de caracteres
bool: Booleano (True o False)
list: Lista
dict: Diccionario
set: Conjunto
tuple: Tupla
None: Representa la ausencia de valor
Optional: Indica que un valor puede ser de un tipo específico o None
Union: Permite indicar que un valor puede ser de varios tipos
Callable: Indica que una función es una función de Python
"""