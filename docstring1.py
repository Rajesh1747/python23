class Calculator:
    """
    A simple calculator class for basic arithmetic operations.

    Usage:
    calculator = Calculator()
    result = calculator.add(5, 3)  # Adds 5 and 3
    print(result)  # Prints 8.0 (as a float)

    Methods:
    - add(x, y): Adds two numbers.
    - subtract(x, y): Subtracts y from x.
    - multiply(x, y): Multiplies two numbers.
    - divide(x, y): Divides x by y.

    Attributes:
    - result (float): The current result of the calculator.
    """

    def __init__(self):
        self.result = 0.0  # Initialize the result as a float

    def add(self, x, y):
        """
        Adds two numbers.

        :param x: The first number (int or float).
        :param y: The second number (int or float).
        :return: The result of the addition (float).
        """
        self.result = float(x + y)
        return self.result

    def subtract(self, x, y):
        """
        Subtracts y from x.

        :param x: The first number (int or float).
        :param y: The second number (int or float).
        :return: The result of the subtraction (float).
        """
        self.result = float(x - y)
        return self.result

    def multiply(self, x, y):
        """
        Multiplies two numbers.

        :param x: The first number (int or float).
        :param y: The second number (int or float).
        :return: The result of the multiplication (float).
        """
        self.result = float(x * y)
        return self.result

    def divide(self, x, y):
        """
        Divides x by y.

        :param x: The numerator (int or float).
        :param y: The denominator (int or float).
        :return: The result of the division (float).
        :raises ZeroDivisionError: If y is 0.
        """
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.result = float(x / y)
        return self.result

