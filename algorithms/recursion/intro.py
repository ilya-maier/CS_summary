# An introduction to recursive algorithms

# Returns the factorial of a given number
def factorial(n):
    # base statement
    if n <= 1:
        return 1

    # the recursion
    return n * factorial(n - 1)


# 10! = 3628800
print(factorial(10))
