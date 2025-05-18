to_do = ["Comprar manzana", 
         "Comprar pizza", 
         "Hacer ejercicio", 
         "Escribir programa"]

print("Lista de tareas:")
print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
print(type(numbers))

mixed_list = [1, 2.5, "tres", True, [1, 2, 3]]
print(mixed_list)
print(len(mixed_list))
print("Primer elemento:", mixed_list[0])
print("Ultimo elemento:", mixed_list[-1])

string = "Hola"
print(string[0])
print(string[1])
print(string[-1])

# Slicing
print(mixed_list[1:3])  # [2.5, 'tres']
print(mixed_list[:3])   # [1, 2.5, 'tres']
print(mixed_list[2:])   # [True, [1, 2, 3]]
print(mixed_list[:])    # [1, 2.5, 'tres', True, [1, 2, 3]]

# Concatenación
new_list = mixed_list + [4, 5]
print(new_list)
mixed_list.append(4)
mixed_list.append(5)
print(mixed_list)
mixed_list.insert(0, 0)
print(mixed_list)

# Eliminar elementos
mixed_list.remove(2.5)  
mixed_list.remove('tres')
print(mixed_list)
del mixed_list[0]
print(mixed_list)

numbers = [1, 2, 3, 4, 5]
print("Mayor", max(numbers))
print("Menor", min(numbers))

