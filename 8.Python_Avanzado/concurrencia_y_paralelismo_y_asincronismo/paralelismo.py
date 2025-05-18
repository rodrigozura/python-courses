import multiprocessing

#Función que calcule el cuadrado de un número
def calculate_square(n):
    return n*n

# Bloque principal de ejecucion
if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    #crear un pool, un pool de procesos es un grupo de procesos que se pueden 
    # usar para ejecutar tareas en paralelo
    #multiprocessing.Pool() crea un pool de procesos
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, numbers)

    print(f'Resultados: {results}')