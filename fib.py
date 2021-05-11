def fib_not_recursive(n):  # O(n)
    a = 1
    b = 1
    c = 0

    for _ in range(1, n-1):
        c = a+b
        a = b
        b = c

    return c


def fib(n, memo={}):  # O(n)
    if(n in memo):
        return memo[n]

    if(n < 3):
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def fib_without_memo(n):  # O(2 ^ n)
    if(n < 3):
        return 1

    return fib_without_memo(n - 1) + fib_without_memo(n - 2)  # O(2^n)


print(fib(50))
print(fib_not_recursive(50))
print(fib_without_memo(50))  # Not polinomial doesn't execute in usefull time
