def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The product of {num1} and {num2} is {multiply_numbers(num1, num2)}")
