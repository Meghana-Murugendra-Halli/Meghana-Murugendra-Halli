def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(fib_num)
    return fib_sequence

n = 7
fib_series = fibonacci(n)

print("Fibonacci Series:")
for fib_num in fib_series:
    print(fib_num)

print(f"\nTotal Fibonacci Numbers: {len(fib_series)}")




