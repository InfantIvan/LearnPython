
def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
num = int(input("Enter a non-negative integer: "))
factorial_result = factorial(num)
if factorial_result is not None:
    print(f"The factorial of {num} is {factorial_result}")
