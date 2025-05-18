# Area de un circulo
def calculate_area(base,height):
    """
    Calcula el área de un triángulo
    :param base(float): La base del triángulo
    :param height(float): La altura del triángulo
    :return float: El área del triángulo
    """
    return (base * height) / 2

# Print the area of a triangle
print(calculate_area(5,10)) # 50.0

# Promedio
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    :param numbers(list): A list of numbers
    :return float: The average of the numbers
    """
    return sum(numbers) / len(numbers)

#  Print the average of a list of numbers
print(calculate_average([1, 2, 3, 4, 5])) # 3.0