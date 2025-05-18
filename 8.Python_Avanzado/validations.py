def divide(a: int, b: int) -> float:
    """
    Divide two numbers and return the result.
    :param a: The numerator.
    :param b: The denominator.
    :return: The result of the division.
    """
    #validar qeu ambos parametros sean enteros
    if not isinstance(a,int) or not isinstance(b, int):
        raise TypeError('Ambos parámetros deben ser enteros.')
    
    # Check if the denominator is zero
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

try:
    res = divide(10, '2')
    print(res)
except TypeError as e:
    print(f"TypeError: {e}")

try:
    res = divide(10, 0)
    print(res)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    res = divide(10, 2)
    print(res)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")