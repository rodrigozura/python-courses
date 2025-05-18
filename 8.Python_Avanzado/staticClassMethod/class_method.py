class Counter:
    count = 0
    # con classmethod no hace falta crear una instancia de la clase Counter
    @classmethod 
    def increment(cls):
        cls.count +=1

Counter.increment()
Counter.increment()
print(Counter.count)