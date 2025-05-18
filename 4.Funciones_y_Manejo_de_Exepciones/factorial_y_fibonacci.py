# factorial (N) = N * factorial(N-1)
# caso base: factorial(0) = 1

def factorial(n):
    # print(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

print("-------------")
# Fibonacci
# Fibonacci (N) = Fibonacci(N-1) + Fibonacci(N-2)
# caso base: Fibonacci(0) = 0, Fibonacci(1) = 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))
print("-------------")