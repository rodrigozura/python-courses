"""
En Python, self es una referencia al objeto actual dentro de un 
método de una clase. Se utiliza para acceder a las variables y 
métodos de la clase desde dentro de sus propios métodos. Es un 
requerimiento de la sintaxis en Python, a diferencia de Java o 
JavaScript, donde se usa this para referirse al objeto actual.

La diferencia radica en que en Python es explícitamente pasado 
como primer parámetro en los métodos, mientras que en Java y 
JavaScript es implícito y se refiere al objeto sin necesidad 
de pasarlo como argumento. Esto es clave en la programación 
orientada a objetos, facilitando la manipulación de atributos 
y métodos de la clase.
"""

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Depositado {amount} a {self.account_holder}")
        else:
            print("La cuenta no está activa")
    
    def withdraw(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("No hay suficiente saldo")
        else:
            print("La cuenta no está activa")
            
    def get_balance(self):
        if not self.is_active:
            print("La cuenta no está activa")
            return None
        return print(f'El saldo de {self.account_holder} es {self.balance}')
    
    def deactivate(self):
        self.is_active = False
        print(f"La cuenta de {self.account_holder} ha sido desactivada")

    def activate(self):
        self.is_active = True
        print(f"La cuenta de {self.account_holder} ha sido activada")

account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

account1.deposit(100)
account2.deposit(200)

print(account1.get_balance())
print(account2.get_balance())

account1.withdraw(50)
account2.withdraw(100)

print(account1.get_balance())
print(account2.get_balance())