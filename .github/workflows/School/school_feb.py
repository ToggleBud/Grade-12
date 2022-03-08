#1, 2, 3, 4, 5, 6, 7

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

fib7 = fib(7)

print(fib7)