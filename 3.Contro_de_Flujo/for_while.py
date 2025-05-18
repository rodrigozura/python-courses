numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    print("Aqui i es igual a:", i + 1)

print("-------------")
for i in range(3, 10):
    print("Aqui i es igual a:", i + 1)

print("-------------")

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruta in fruits:
    print("Aqui fruta es igual a:", fruta)
    if fruta == "Uva":
        print("Se ha encontrado la Uva")
        break

print("-------------")
x = 0
while x < 5:
    if x == 3:
        print("Se ha encontrado el 3")
        break
    print(x)
    x += 1

print("-------------")
for i in numbers:
    if i == 3:
        print("Se ha encontrado el 3")
        continue
    print(i)