def factorial(n):
    if(n < 2):
        return n

    return factorial(n-1) * n


print(factorial(20))
