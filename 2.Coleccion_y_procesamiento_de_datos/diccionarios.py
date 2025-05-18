numbers = {"uno": 1, "dos": 2, "tres": 3}
print(numbers)

numbers["cuatro"] = 4
print(numbers)

print("----------")
for key, value in numbers.items():
    print(key, value)

print("----------")
for value in numbers.values():
    print(value)

print("----------")
for key in numbers.keys():
    print(key)

print("----------")
del numbers["dos"]
print(numbers)

numbers["cinco"] = 5
print(numbers)

print("----------")
print(numbers.keys())
print(numbers.values())

print("----------")
contacts = {
    "Juan": {
        "name": "Juan",
        "last_name": "Perez",
        "age": 30,
        "city": "Madrid",
        "country": "España"
    },
    "Maria": {
        "name": "Maria",
        "last_name": "Perez",
        "age": 30,
        "city": "Madrid",
        "country": "España"
    },
    "Pedro": {
        "name": "Pedro",
        "last_name": "Gomez",
        "age": 30,
        "city": "Madrid",
        "country": "España"
    }
}

print(contacts)
print("----------")
print(contacts["Juan"])