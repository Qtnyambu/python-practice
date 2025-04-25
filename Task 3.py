number = int(input("Enter a number: "))

def factorial_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1

    return factorial
result = factorial_loop(number)
print(f"The factorial is: {result}")
##for our loop  we will use while to show how factorial works
