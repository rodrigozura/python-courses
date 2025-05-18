a = [1, 2, 3, 4, 5]
b = a
print(a)
print(b)

del a[0]
print(a)
print(b)

del b[0]
print(a)
print(b)

# apuntan al mismo espacio de memoria, x eso se borran
print(id(a))
print(id(b))

c = a[:]

print(id(c))

a.append(6)
print(a)
print(b)
print(c)
