print('-- Help: type quit to exit from the program')
while True:
    name=input('Enter any name :')
    if name.lower()=='quit':
        break

print("\n odd number :\n")
for number in range(10):
    if number%2==0:
        continue
    print(number)
    
print("\n Even number :\n")
for number in range(10):
    if number%2:
        continue
    print(number)