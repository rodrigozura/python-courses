class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        # Devuelve una representación amigable para el usuario
        return f"Persona: {self.nombre}, {self.edad} años"

    def __repr__(self) -> str:
        # Devuelve una representación detallada del objeto para depuración
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    def __eq__(self, otra_persona) -> bool:
        # Compara si dos personas son iguales en función del nombre y la edad
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    def __lt__(self, otra_persona) -> bool:
        # Compara si una persona es "menor" que otra en función de la edad
        return self.edad < otra_persona.edad

    def __add__(self, otra_persona):
        # Sobrecarga el operador + para sumar las edades de dos personas
        return self.edad + otra_persona.edad

# Crear instancias de Persona
p1 = Persona("Ana", 28)
p2 = Persona("Luis", 35)
p3 = Persona("Ana", 28)

# __str__: Representación legible
print(p1)  # Output: Persona: Ana, 28 años

# __repr__: Representación detallada
print(repr(p2))  # Output: Persona(nombre='Luis', edad=35)

# __eq__: Comparación de igualdad
print(p1 == p3)  # Output: True (son iguales en nombre y edad)

# __lt__: Comparación "menor que" por edad
print(p1 < p2)  # Output: True (porque 28 es menor que 35)

# __add__: Sumar edades de dos personas
print(p1 + p2)  # Output: 63 (28 + 35)



# ------------------------------------------------------------------------------
"""
Imagina que tienes una caja de juguetes muy especial. Esta caja 
tiene algunos juguetes mágicos que pueden hacer cosas increíbles 
cuando juegas con ellos de ciertas maneras. Los métodos mágicos 
en Python son como esos juguetes especiales. Son funciones que 
empiezan y terminan con dos guiones bajos (__) y permiten que los 
objetos de tus clases hagan cosas mágicas.

Por ejemplo, cuando sumas dos números con el signo +, Python usa 
un método mágico llamado __add__
"""
class Juguete:
    def __init__(self, nombre):
        self.nombre = nombre

    def __add__(self, otro_juguete):
        return Juguete(self.nombre + " y " + otro_juguete.nombre)

# Crear dos juguetes
juguete1 = Juguete("Carro")
juguete2 = Juguete("Avión")

# Usar el método mágico __add__ para "sumar" los juguetes
juguete3 = juguete1 + juguete2

print(juguete3.nombre)  # Salida: Carro y Avión


# ------------------------------------------------------------------------------
"""
Los **métodos mágicos** en Python (también llamados "métodos especiales" o 
"dunder methods" por la doble subrayado que los rodea) son funciones predefinidas 
en las clases que permiten personalizar el comportamiento de los objetos en varias 
situaciones, como en operaciones matemáticas, conversiones de tipos, comparaciones 
y manejo de contenedores.

Estos métodos comienzan y terminan con doble subrayado (\_\_), por ejemplo, 
\_\_init\_\_ o \_\_str\_\_. Al definir estos métodos, se le puede indicar a Python 
cómo debe comportarse un objeto en distintos contextos.

### 1. Métodos de Inicialización y Representación

- **\_\_init\_\_(self, ...)**: Inicializador de una clase (similar a un constructor). 
Se ejecuta al crear una instancia.

- **\_\_str\_\_(self)**: Define el comportamiento del objeto cuando se convierte 
a una cadena con str(), como al usar print().

- **\_\_repr\_\_(self)**: Representación oficial del objeto, útil para depuración. 
A menudo se usa en lugar de \_\_str\_\_ para generar un mensaje detallado y debe 
proporcionar una salida que permita recrear el objeto cuando se usa eval().

"""

class Persona2:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona({self.nombre}, {self.edad})"

    def __repr__(self):
        return f"Persona(nombre={self.nombre!r}, edad={self.edad})"

persona = Persona2("Ana", 30)
print(persona) # Salida personalizada
repr(persona) # Representación oficial para depuración

"""
### 2. Métodos de Operadores Aritméticos

Permiten personalizar el comportamiento de operadores (+, -, \*, /, etc.).

- **\_\_add\_\_(self, other)**: Define el comportamiento de la adición (self + other).

- **\_\_sub\_\_(self, other)**: Define la resta (self - other).

- **\_\_mul\_\_(self, other)**: Define la multiplicación (self \* other).

- **\_\_truediv\_\_(self, other)**: Define la división (self / other).
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 5)
print(v1 + v2) # Salida: Vector(3, 8)

"""
### 3. Métodos de Comparación

Permiten especificar el comportamiento para comparaciones (==, <, >, etc.).

- **\_\_eq\_\_(self, other)**: Define la comparación de igualdad (self == other).

- **\_\_lt\_\_(self, other)**: Define la comparación de "menor que" (self < other).

- **\_\_le\_\_(self, other)**: Define la comparación de "menor o igual" (self <= other).
"""

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        return self.edad == other.edad

    def __lt__(self, other):
        return self.edad < other.edad

persona1 = Persona("Juan", 25)
persona2 = Persona("Ana", 30)
print(persona1 == persona2) # Salida: False
print(persona1 < persona2) # Salida: True

"""

### 4. Métodos de Acceso a Elementos

Permiten definir el comportamiento de acceso, modificación y eliminación de 
elementos en objetos como si fueran contenedores.

- **\_\_getitem\_\_(self, key)**: Define el comportamiento al acceder a 
un elemento (self\[key]).

- **\_\_setitem\_\_(self, key, value)**: Define el comportamiento al asignar 
un valor (self\[key] = value).

- **\_\_delitem\_\_(self, key)**: Define el comportamiento al eliminar un 
elemento (del self\[key]).

"""

class Contenedor:

    def __init__(self):
        self.datos = {}

    def __getitem__(self, key):
        return self.datos.get(key, None)

    def __setitem__(self, key, value):
        self.datos[key] = value
    def __delitem__(self, key):
        del self.datos[key]

cont = Contenedor()
cont["a"] = 10
print(cont["a"]) # Salida: 10
del cont["a"]

"""

### 5. Métodos de Contexto (con with)

Permiten definir el comportamiento al usar un objeto con el bloque with, 
como al manejar archivos.

- **\_\_enter\_\_(self)**: Inicializa o prepara el objeto para el contexto.

- **\_\_exit\_\_(self, exc\_type, exc\_val, exc\_tb)**: Define el comportamiento 
al salir del contexto, manejando cualquier excepción.

"""

class Archivo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = None

    def __enter__(self):
        self.archivo = open(self.nombre, "w")
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()

with Archivo("ejemplo.txt") as f:
    f.write("Texto de ejemplo")

"""

### Resumen

Los métodos mágicos permiten una gran personalización y facilitan la creación de 
clases que se comportan de forma coherente con los operadores y funciones de Python. 
Al definir estos métodos, puedes hacer que las clases respondan a operaciones y 
funciones nativas de Python, logrando una sintaxis más intuitiva y adaptada a tus 
necesidades.


"""