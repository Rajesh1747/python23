age=int(input("Enter your age : "))
if(age%100==0) or (age%1==0 and age%10!=0):
    print("Given age is leaf " ,age)
else:
    print("Given age is not leaf " ,age)
    
