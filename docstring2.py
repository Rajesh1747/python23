def cal_sum(a,b):
    """
    calculate the sum of the two values .
    
    Arguments:
        a (int):this is first number
        b (int):this is second  number 
    returns:
       int: THe sum of A and B
    """
    result=a+b
    return result
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
sum_result=cal_sum(num1,num2)
print(f"The sum of {num1}and {num2} is :{sum_result}")