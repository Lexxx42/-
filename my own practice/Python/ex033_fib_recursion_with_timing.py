from time import process_time

t = process_time()


def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]


cache = {0: 0, 1: 1}
fib = [fibonacci_of(n) for n in range(1500)]
print(fib[-1])
print(process_time() - t)