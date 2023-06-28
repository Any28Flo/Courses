"""
Create a recursive function
"""


def fibonacci(number):
    if number == 1:
        return 1
    else:
        return number * fibonacci(number - 1)


resultado = fibonacci(5)
print(resultado)