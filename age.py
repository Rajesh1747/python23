age = int (input("Enter your age here "))
if(age<10):
    print("The child age",age)
else:
    if(age<18):
        print("The adult age",age)
    else:
        if(age<27):
            print("The middle age",age)
        else:
            if(age<50):
                print("The older age",age)