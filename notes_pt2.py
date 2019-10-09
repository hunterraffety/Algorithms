# fibonacci sequence
cache = {}
def dynamic_fib(n):
    global cache
    if n < 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        cache[n] = dynamic_fib(n - 1) + dynamic_fib(n - 2)
        return cache[n]

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(dynamic_fib(32))
print(fib(32))

print(cache)