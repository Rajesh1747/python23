Name=str(input("person name : "))
age=int(input("person age : "))
print("person Name : ",Name)
print("person age : ",age)
if(age<10):
    print("child")
else:
    if(age<28):
        print("Adult")
    else:
        if(age<40):
            print("middle")
        else:
            if(age<60):
                print("oldage")

