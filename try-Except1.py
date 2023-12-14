# code that may cause an exception 
x=int(input("Enter the value  : "))
try:
    result=10/x
    print("Result",result)
except ZeroDivisionError :
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
finally:
    print("Execution completed, regardless of exceptions.")