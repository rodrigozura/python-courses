"""
Los decoradores en Python son funciones que modifican el comportamiento
de otras funciones o métodos. Son una herramienta muy útil para añadir 
funcionalidades o preprocesamientos sin tener que cambiar el código 
original de la función decorada.

### ¿Qué es un Decorador?

Un decorador es una función que toma otra función como argumento y le añade 
funcionalidades adicionales. Devuelve una nueva función modificada o envuelta 
con el comportamiento adicional.
"""


def log_transaction(func):
    def wrapper():
        print('1 Log de la transacción...')
        func()
        print('3 Log terminado...')
    return wrapper
        
# Es como que @log_transaction indicara que la función process_payment
# debe ser envuelta con el decorador log_transaction
# En este caso, el decorador log_transaction añade un comportamiento
# adicional al procesar_payment
# func() seria la funcion process_payment
@log_transaction
def process_payment():
    print('2 Procesando pago....')

process_payment()