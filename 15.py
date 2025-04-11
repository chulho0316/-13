# Fibonacci numbers module
fib(1000)
def fib2(n): # write Fibonacci series up to n
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result
resultList = fib2(1000)
print(resultList)

import fibonacci as fib3
resultList[:] = []
resultList = fib3(1000)
print(resultList)

# fibonacci.py
def fibonacci(n): #return fibonacci
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
        return result
