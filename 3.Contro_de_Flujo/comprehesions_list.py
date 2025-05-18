# List Comprehensions: [expresion for item in terable if condicion]

print("---------Cuadrados---------")
squares = [x**2 for x in range(1,11)]
print("Cuadrados:", squares)

print("---------Temperatura en F---------")
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius]
print("Temperatura en F:", fahrenheit)

print("---------Numeros pares---------")
#Numeros pares
evens = [x for x in range(1,21) if x%2 ==0]
print(evens)


print("---------Matriz transponed---------")
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("Matriz original:", matrix)
print("Matriz transponed:", transposed)

# Lo mismo de arriba pero sin comprension de listas
# compprehesions list nos ayuda a escribir menos lineas de codigo y menor tiempo de ejecucion
transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)