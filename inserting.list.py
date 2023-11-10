number=[1,2,3,4,5,6,7]
number.insert(3,400)
print(number)

# Import the module and print its docstring
def my_modules(x,y):
    x=input("enter thw value")
    y=input("enter the value ")

# Create a module named my_module.py with the following content:
"""
This is a module that contains some useful functions.

Functions:
    add(x, y): Returns the sum of x and y.
    subtract(x, y): Returns the difference of x and y.
    multiply(x, y): Returns the product of x and y.
    divide(x, y): Returns the quotient of x and y.
"""

def add(x, y):
    d = x+y
    """Returns the sum of x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    return d
print(add(1,2))

def subtract(x, y):
    d =x-y
    """Returns the difference of x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The difference of x and y.
    """
    return d
print(subtract(1,2))
def multiply(x, y):
        a=x*y
        """
    Returns the product of x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The product of x and y.
    """
    return a
print("multiply(x,y)")
print(multiply(1,2))

def divide(x, y):
        d =x/y
        """Returns the quotient of x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        float: The quotient of x and y.
    """
    return d
print(divide(x,y))
