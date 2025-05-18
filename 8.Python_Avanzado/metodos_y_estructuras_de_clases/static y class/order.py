class Order:

    # @staticmethod es un decorador que nos permite poder 
    # llamar a un método de clase sin crear una instancia
    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount * (tax_rate / 100)
    
print(Order.calculate_tax(1000, 18))