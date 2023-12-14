#try-except Handiling-ZeroDivisionError
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")