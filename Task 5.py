def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n - 1)
print (factorial(5))
## we use the n==0 as the base case and recall the factorial function in the else section