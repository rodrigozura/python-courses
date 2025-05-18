# SyntaxError
# TypeError
# ZeroDivisionError
# try:
#     divisor = int(input("Introduce un divisor: "))
#     result = 100 / divisor
#     print(f"El resultado es: {result}")
# except ZeroDivisionError as e:
#     print("Error: No se puede dividir entre cero")
#     print(e)
# except ValueError as e:
#     print("Error: El divisor debe ser un numero entero")
#     print(e)


def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)