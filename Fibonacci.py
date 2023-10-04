def generate_fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

print("Fibonacci Generator")
n = int(input('Enter a number terms to find it Fibonacci series: '))
result = generate_fibonacci(n)
print(result)
