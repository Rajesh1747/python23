age=int(input("Enter the age : "))
print("person age",age)
if(age<12):
    print(" child ")
else:
    if(age<28):
        print("Adult")
    else:
        if(age<40):
            print("middle")
        else:
            print("oldage")
