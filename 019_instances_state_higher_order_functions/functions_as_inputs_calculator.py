def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Higher order function - a function that work with other functions.
# In this case, calculator is a higher order function.

def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(2, 3, add)
print(result)