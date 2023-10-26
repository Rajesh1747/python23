a=60 #tel=10
b=30 #hin=39
c=600 #eng=40 
if(a>b and a>c): 
    print("\n A is biggest value then B and C ",a)
else:
    if(b>c and b>c):
     print("\n B is biggest value then A and c ",b)
    else:
       print("\n c is biggest value then a and b",c)

#lowestvalue 
tel=1100
hin=306
mat=540
if(tel<hin and tel<mat):
    print("the value hin and mat",tel)
else:
    if(hin<tel and hin<mat):
        print("the value tel and mat",hin)
    else:
        print("the value tel and hin",mat)
#higestvalue
tel=1100
hin=306
mat=540
if(tel>hin and tel>mat):
    print("the value hin and mat",tel)
else:
    if(hin>tel and hin>mat):
        print("the value tel and mat",hin)
    else:
        print("the value tel and hin",mat)


#all the lowest,higest,percentage,total,smallest
telugu=99
english=85
sanskrit=73
maths=89
social=61
if(telugu>english and telugu>sanskrit and telugu>maths and telugu>social):
	print("The higest marks telugu",telugu)
else:
	if(english>telugu and english>sanskrit and english>maths and english>social):
		print("The higest marks english",english)
	else:
		if(sanskrit>telugu and sanskrit>english and sanskrit>maths and sanskrit>social):
			print("The higest marks sanskrit",sanskrit)
		else:
			if(maths>telugu and maths>sanskrit and maths>english and maths>social):
				print("The higest marks maths",maths)
			else:
				print("The higest marks social",social)
total=telugu+english+sanskrit+maths+social
print("The total marks of all subjects",total)
percentage=total/5
print("The percentage",percentage)
if(telugu<english and telugu<sanskrit and telugu<maths and telugu<social):
	print("The lowest marks telugu",telugu)
else:
	if(english<telugu and english<sanskrit and english<maths and english<social):
		print("The lowest marks english",english)
	else:
		if(sanskrit<telugu and sanskrit<english and sanskrit<maths and sanskrit<social):
			print("The lowest marks sanskrit",sanskrit)
		else:
			if(maths<telugu and maths<sanskrit and maths<english and maths<social):
				print("The lowest marks maths",maths)
			else:
				print("The lowest marks social",social)
if(telugu<50):
	print("The smallest marks telugu",telugu)
else:
	if(english<50):
		print("The smallest marks english",english)
	else:
		if(sanskrit<50):
			print("The smallest marks sanskrit",sanskrit)
		else:
			if(maths<50):
				print("The smallest marks maths",maths)
			else:
				print("The smallest marks social",social)


#Type of conversion
value=input("enter a value:")
print(value)


#input value 
telugu= int (input("the telugu subject marks"))
hindi=int (input("the hindi subject marks"))
english=int (input("the english subject marks"))
social=int (input("the social subject marks"))
science=int (input("the science subject marks"))

print("/n telugu subjects marks",telugu)
print("/n hindi subjects marks",hindi)
print("/n english subjects marks",english)
print("/n social subjects marks",social)
print("/n science subjects marks",science)

total=telugu+hindi+english+social+science
print("the total value of all 5 subjects",total)
average=total/5
print("/n the average value of all subjects",average)

if(telugu>hindi and telugu>english and telugu>social and telugu>science):
	print("The higest marks telugu",telugu)
else:
	if(hindi>telugu and hindi>english and hindi>social and hindi>science):
		print("The higest marks hindi",hindi)
	else:
		if(english>hindi and english>telugu and english>social and english>science):
			print("The higest marks english",english)
		else:
			if(social>hindi and social>english and social>telugu and social>science):
				print("The higest marks social",social)
			else:
				print("The higest marks science",science)
if(telugu<hindi and telugu<english and telugu<social and telugu<science):
	print("The lowest marks telugu",telugu)
else:
	if(hindi,telugu and hindi<english and hindi<social and hindi<science):
		print("The lowest marks hindi",hindi)
	else:
		if(english<hindi and english<telugu and english<social and english<science):
			print("The lowest marks english",english)
		else:
			if(social<hindi and social<english and social<telugu and social<science):
				print("The lowest marks social",social)
			else:
				print("The lowest marks science",science)
if(telugu<35):
	print("The failed subject telugu",telugu)
else:
	if(hindi<35):
		print("The failed subject hindi",hindi)
	else:
		if(english<35):
			print("The failed subject english",english)
		else:
			if(science<35):
				print("The failed subject science",science)
			else:
				print("The failed subject social",social)



# float values
a = float(input("Enter a number"))
b = float(input("Enter another number"))
 
sum = a + b
print("sum of {0} and {1} is {2}" .format(a, b, sum))


#to creat a login page 
login= int,str,float(input("login id"))
password= int,float,str(input("password"))
print("login",login)
print("password",password)


#Name age of person 
name = str(input(" Name : "))
age = int(input(" age  : "))
print("name of person : ",name)
print("age of person : ",age)
if (age < 12):
    print("Child")
else:
    if(age < 18):
        print:("Teen")
    else:
        if(age < 26):
            print("Adult")
        else:
            if(age < 40):
                print("middle")
            else:
                if(age > 60):
                    print("oldage")
                    
#using float and elif
number = float(input(" number : "))
print("positive or negative number")
if(number > 0):
    print("positive number")
elif (number == 0):
    print("zero")
else:
    print("negative number") 

#The natural numbers
for index in range(10):
    print("/n The natural number : ",index+1)

#To get even numbers
for index in range (0,20, 2):
    print("Even numbes :  ", index)

#To print sum of 10 natural numbers
sum=0
for num in range(10):
    sum+=num
    print("/n The sum of 10 natural numbers : ",sum) 

#To print 

|number=int(input("sum : "))
sum=0
for num in range(number):
    sum+=num
print("/n The sum of 10 natural numbers : ",sum) 


#To find give year is leaf year or not
year=int(input("Enter any year "))
if(year%400==0) or (year%4==0 and year%100!=0):
    print("/n Given year is leap year : ",year)
else:
    print("/n Given year is not leap year : ",year)

#To find give year is leaf year or not
import calendar
year=int(input("/n Enter year : "))
isLeap=calendar.isleap(year)
if isLeap:
    print("/n Given year is Leap year : ",year)
else:
    print("/n Given yera is notleap year :",year)

#Even or odd number
   number=int(input("Enter any number : "))
if number%2==0:
    print("Given number is Even :",number)
else:
    print("Given number is odd :",number)

#prime number 
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

#The tables 
number=4
for i in range(1,11):
    print(number, 'x',i, '=',number*i)

#Enter the input value
number=int(input("Enter the number : "))
for i in range(1,11):
    print(number, 'x',i, '=',number*i)

#Tables of 1 to 10
for i in range(1,11):
    print("\n The multipliction table of %d\n" %(i))
    for j in range(1,11):
        print("%-5d x %5d = %5d" % (i , j ,i*j))

#Enter the input value
start=int(input("Enter the number : "))
for i in range(1,start+1):
    print("\n The multipliction table of %d\n" %(i))
    for j in range(1,11):
        print(i , '*', j, "=" , i*j)

#while loop 
number=6
count=0
while count < number:
    print(count)
    count+= 1        

#while loop 
number=int(input("Enter the number : "))
count=0
while count < number+1:
    print(count)
    count+= 1   

#sum of n natural number
number=int(input("Enter a number"))
i=1
sum=0;
while (i<=number) :
    sum=sum+i
    i=i+1
print("The sum of natural numbers",sum)


#write a python program to print sum of n natural numbers 
number=int(input("Enter a number : "))
if number<0:
    print("enter a positive numbers")
else:
    sum=0
    while(number>0):
        sum+=number
        number -=1
        print("The result value is ",sum)

#write a python program tomprint all even numbers in given range 
start,end=1,100
for number in  range (start,end+1):
    if number %2==0:
        print(number , end= " ")

#Even numbers
number=2
while number<=100:
    print(number)
    number=number+2


 #To get the range numbers   
for number in range(0,100):
    print(number)
    if number==40:
        break   
#range and break
for x in range(5):
    for y in range(5):
        if y>1:
            break
        print(f"({x}.{y})")

#Enter the name and quit
print('-- Help: type quit to exit from the program')
while True:
    name=input('Enter any name :')
    if name.lower()=='quit':
        break

#odd number continue
print("\n odd number :\n");   
for number in range(100):
    if number%2==0:
        continue
    print(number)

#Even number continue
print("\n Even number :\n")
for number in range(100):
    if number%2:
        continue
    print(number)


#ternary operator 
age=input("\n Enter your age :")
if int(age)>=18:
    ticket_price=40
else:
    ticket_price=20
    print(f"The ticket pricr is {ticket_price}")

#False statement (syntos error)
counter=1
max=10
if counter<=max:
    counter+=1
else:
    pass

#by singel quotes
message='Hi this is Sandy'
print("This is single quotes message"message)  


#by Double quotes
message="Hi this is Sandy"
print("THis is double quotes message "message)  

#Text in quotes on output 
message="Hi this is Sandy"
print(message)

#multiline Text message 
message='''
hi
this is rajesh'''
print(message)


#string concatenation
string1=hi
string2=good morning
greeting=string1+string2
print(greeting)

#string Length by len Function 
str="python string"
print(str[1])
print(str[3])
print(str[8])
print(str[2])

#string Length by len Function output 
str=input("Enter the name : ")
print(str[1])
print(str[3])
print(str[4])
print(str[2])

#To find given String length
str="Clpud Gensoftech"
str_len=len(str)
print(" Given Cloud GEnsoftech String length is ",str_len)
print("\n\n\n\n\n");

#To get slicing string by memory of arrays 
str="cloud Gen"
print(str[0:3])

#function
def greet (name):
	print("HI {name}")
	greet('rajesh')

#function Return 
def greet (name):
	return f"hi{name}"
greeting=greet('cloud Gen')
print(greeting)

#sum of the two values by using function 
def sum(a,b):
	return a+b
total=sum(10,20)
print("The of the two values", total)

#default parameters in python function program
def greet (name,message="hi i am rajesh "):
	return f"{message} {name}"
greeting=greet('vyas')
print(greeting)

#multiple Default marameters values in python Function 
def greet {name='hi Rajesh',message='how are you'}:
	return f"{name} {message}"
	greeting=greet()
	print(greeting)
