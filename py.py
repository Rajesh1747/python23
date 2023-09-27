marks=[72,56,81,98]

max_number = 0
min_number = 100

for i in marks :
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i
        
print("Highest marks:",max_number)
print("lowest marks",min_number)            