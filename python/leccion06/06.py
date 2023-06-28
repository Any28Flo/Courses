"""
    Create a function to
"""


def fibonacci(number):
    if number >= 1:
        print(number)
        return number - fibonacci(number - 1)
    elif number == 0:
        print("** Num no valido **")
    elif number <= 0:
        print("** Num no valido **")


resultado = fibonacci(0)
print(resultado)
