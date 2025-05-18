class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Herencia
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # Overriding the greet method
    # This in POO is called polymorphism
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        print(f"My student ID is {self.student_id}")

person1 = Person("Alice", 30)
person2 = Student("Bob", 25, "12345")

print(person1.name)
print(person2.name)
print(person1.age)
print(person2.age)

person1.greet()
person2.greet()


# Super level 3
class LivingBeing:
    def __init__(self, name):
        self.name = name


class Person2(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student2(Person2):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        print(f"My student ID is {self.student_id}")


