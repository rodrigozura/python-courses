class Order:
    global_discount = 10

    def __init__(self,amount):
        self.amount = amount

    # @classmethod es un decorador que nos permite poder
    # llamar a un método de clase sin crear una instancia
    # la diferencia de staticmethod, este método recibe como primer argumento
    # la clase en vez de la instancia
    @classmethod
    def update_gloabal_discount(cls, new_discount):
        cls.global_discount = new_discount

Order.update_gloabal_discount(15)
print(Order.global_discount)
        
        
