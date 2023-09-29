child = int (input("Enter your child age here "))
adult = int (input("Enter your adult age here "))
middle = int (input("Enter your middle age here "))
oldage = int (input("Enter your oldage here "))
print("The child age",child)
print("The adult age",adult)
print("The middle age",middle)
print("The older age",oldage)
if(child<10):
    print("The child age",child)
else:
    if(adult<18):
        print("The adult age",adult)
    else:
        if(middle<27):
            print("The middle age",middle)
        else:
            if(oldage<50):
                print("The older age",oldage)
if(child>10):
    print("The child age",child)
else:
    if(adult>18):
        print("The adult age",adult)
    else:
        if(middle>27):
            print("The middle age",middle)
        else:
            if(oldage>50):
                print("The older age",oldage)

