class Person:
    # Constructor
    # Initialize the attributes of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name)
print(person2.name)
print(person1.age)
print(person2.age)

person1.greet()
person2.greet()