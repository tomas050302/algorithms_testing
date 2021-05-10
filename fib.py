def fib(n, memo={}):
    if(n in memo):
        return memo[n]

    if(n < 3):
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)  # O(n)
    return memo[n]


def fib_without_memo(n):
    if(n < 3):
        return 1

    return fib_without_memo(n - 1) + fib_without_memo(n - 2)  # O(2^n)


print(fib_without_memo(501))
