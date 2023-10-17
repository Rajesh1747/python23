number=int(input("enter any number : "))
flag=1
for i in range(2, int(number/2)):
    if number%i==0:
        flag=0
        beak
if flag==1 and number>=2:
    print("Given number is prime number  ",number)
else:
    print("Given number is even number ",number)