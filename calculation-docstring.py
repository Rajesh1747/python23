class Calculator:
    num1=float(input("Enter the x value : "))
    num2=float(input("Enter the y value "))
    """
    This class provides basic arithmetic operations.
    
    Attributes:
        result (float): The current result of calculations.
    """
    
    def add(self, num1,num2):
        """
        Add a number to the current result.
        Args:
            num (float): The number to add.
        """
    self_add = num1+num2
    print(f"The sum of {num1} and {num2} are : {self_add} ")

   
    def subtract(self, num1,num2):
        """
        Subtract a number from the current result.
        Args:
            num (float): The number to subtract.
        """
        self_subtract = num1-num2
        print(f"The subtract of {num1} and {num2} are : {self_subtract} ")