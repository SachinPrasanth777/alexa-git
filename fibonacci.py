def generate_fibonacci(n):
    if n <= 0: return "Enter a positive integer."
    if n == 1: return [0]
    if n == 2: return [0, 1]
    fib = [0, 1]
    for i in range(2, n): fib.append(fib[-1] + fib[-2])
    return fib

print(generate_fibonacci(int(input("Enter the number of terms: "))))
