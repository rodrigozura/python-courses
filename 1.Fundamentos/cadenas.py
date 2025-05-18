name = 'Rodrigo' # str
print(name) # Imprime el valor de la variable name
print(type(name)) # Imprime el tipo de la variable name

name = '''Rodrigo

Zurita''' # str estas no son sensibles a los espacios en blanco
print(name) # Imprime el valor de la variable name
print(type(name)) # Imprime el tipo de la variable name

name = "Rodrigo Zurita" # str
print(name[0]) # Imprime el primer caracter de la variable name
print(name[1:4]) # Imprime el valor de la variable name desde el segundo caracter hasta el cuarto caracter
print(name[1:]) # Imprime el valor de la variable name desde el segundo caracter hasta el final
print(name[-3]) # Imprime desde el final el tercer caracter

last_name = 'Zurita' # str
first_name = 'roDrigo' # str
full_name = first_name + ' ' + last_name # str
print(full_name) # Imprime el valor de la variable full_name
print(f'{first_name} {last_name}') # Imprime el valor de la variable full_name usando f-strings
print(len(full_name)) # Imprime la longitud de la variable full_name
print(full_name.upper()) # Imprime el valor de la variable full_name en mayúsculas
print(full_name.lower()) # Imprime el valor de la variable full_name en minúsculas
print(full_name.title()) # Imprime el valor de la variable full_name en formato título
print(full_name.strip()) # Elimina los espacios en blanco al principio y al final de la variable full_name