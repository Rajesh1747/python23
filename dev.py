Telugu = int(input("Enter Telugu Marks : "))

Hindi = int(input("Enter HIndi Marks : "))

English = int(input("Enter English Marks : "))

Maths = int(input("Enter Maths Marks : "))

Science = int(input("Enter Science Marks : "))

Social = int(input("Enter Social Marks : "))

Total_Marks = Telugu + Hindi + English + Maths + Science + Social

print("Total Marks:", Total_Marks)

Percentage=(Total_Marks/680)

print (Percentage)

data={'Telugu': Telugu, 'Hindi' :Hindi, 'English': English, 'Maths': Maths, 'Science' : Science, 'Social': Social}

max_value_key = max(data, key=data.get)

max_value = data[max_value_key]

print("the highest marks sub is {max_value_key } and marks got in that sub is {max_value}")

min_value_key= min(data, key=data.get)

min_value = data[min_value_key]

print(f" the lowest marks sub is {min_value_key} and Marks got in that sub is {min_value}")


if(min_value<35):
    print('Fail')
else:
    print('pass')