#Enter the input value
start=int(input("Enter the number : "))
for i in range(1,start+1):
    print("\n The multipliction table of %d\n" %(i))
    for j in range(1,11):
        print(i , '*', j, "=" , i*j)