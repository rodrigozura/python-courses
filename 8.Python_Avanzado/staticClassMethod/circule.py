# @property lo que hace es ayudarnos a acceder a un metodo pero como si fuera un atributo
# @radius.setter lo que hace es cambiar el valor de la propiedad radius
class Circle:
    #  Constructor
    def __init__(self, radius: float):
        self._radius = radius
    
    @property
    def area(self) -> float:
        return 3.1416 * self._radius ** 2
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("El radio debe ser mayor que cero")
        self._radius = value

circle = Circle(5)
print(circle.area)
print(circle.radius)
circle.radius = 10
print(circle.area)
# circle.radius = -5  # Esto lanzará un ValueError
# print(circle.radius)
# print(circle.area)

