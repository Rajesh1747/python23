[200~1. Python program to check whether the given number is even or not.

        number = input("Enter a number: ")
        x = int(number)%2
        if x == 0:
            print("The number is Even.")
            else:
                print("The number is Odd.")
                Output:

                Enter a number: 7
                The number is Odd.
                Enter a number: 6
                The number is Even.

                2. Python program to convert the temperature in degree centigrade to Fahrenheit

                c = input("Enter temperature in Centigrade: ")
                f = (9*(int(c))/5)+32
                print("Temperature in Fahrenheit is: ", f)
                Output:

                Enter temperature in Centigrade: 30
                Temperature in Fahrenheit is:  86.0

                3. Python program to find the area of a triangle whose sides are given

                import math
                a = float(input("Enter the length of side a: "))
                b = float(input("Enter the length of side b: "))
                c = float(input("Enter the length of side c: "))
                s = (a+b+c)/2
                area = math.sqrt(s*(s-a)*(s-b)*(s-c))
                print("Area of the triangle is: ", area)
                Output:

                Enter the length of side a: 4.0
                Enter the length of side b: 3.0
                Enter the length of side c: 6.0
                Area of the triangle is:  5.332682251925386

                4. Python program to find out the average of a set of integers

                count = int(input("Enter the count of numbers: "))
                i = 0
                sum = 0
                for i in range(count):
                    x = int(input("Enter an integer: "))
                        sum = sum + x
                        avg = sum/count
                        print("The average is: ", avg)
Output:

    Enter the count of numbers: 5
    Enter an integer: 3
    Enter an integer: 6
    Enter an integer: 8
    Enter an integer: 5
    Enter an integer: 7
    The average is:  5.8

    5. Python program to find the product of a set of real numbers

    i = 0
    product = 1
    count = int(input("Enter the number of real numbers: "))
    for i in range(count):
            x = float(input("Enter a real number: "))
                product = product * x
                print("The product of the numbers is: ", product)
                Ezoic
                Output:

                    Enter the number of real numbers: 4
                    Enter a real number: 3.2
                    Enter a real number: 2.9
                    Enter a real number: 7.4
                    Enter a real number: 5.5
                    The product of the numbers is:  377.69599999999997

                    6. Python program to find the circumference and area of a circle with a given radius

                    import math
                    r = float(input("Input the radius of the circle: "))
                    c = 2 * math.pi * r
                    area = math.pi * r * r
                    print("The circumference of the circle is: ", c)
                    print("The area of the circle is: ", area)
                    Output:

                        Input the radius of the circle: 4.3
                        The circumference of the circle is:  27.01769682087222
                        The area of the circle is:  58.088048164875275

                        7. Python program to check whether the given integer is a multiple of 5

                        number = int(input("Enter an integer: "))
                        if(number%5==0):
                                print(number, "is a multile of 5")
                            else:
                                    print(number, "is not a multiple of 5")
                                    Output:

                                        Enter an integer: 23
                                        23 is not a multiple of 5
                                        Enter an integer: 55
                                        55 is a multile of 5

                                        8. Python program to check whether the given integer is a multiple of both 5 and 7

                                        number = int(input("Enter an integer: "))
                                        if((number%5==0)and(number%7==0)):
                                                print(number, "is a multiple of both 5 and 7")
                                            else:
                                                    print(number, "is not a multiple of both 5 and 7")

                                                    Ezoic
                                                    Output:

                                                        Enter an integer: 33
                                                        33 is not a multiple of both 5 and 7
                                                        Enter an integer: 35
                                                        35 is a multiple of both 5 and 7

                                                        9. Python program to find the average of 10 numbers using while loop

                                                        count = 0
                                                        sum = 0.0
                                                        while(count<10):
                                                                number = float(input("Enter a real number: "))
                                                                    count=count+1
                                                                        sum = sum+number
                                                                        avg = sum/10
                                                                        print("Average is :",avg)
                                                                        Output:

                                                                            Enter a real number: 2.3
                                                                            Enter a real number: 3.3
                                                                            Enter a real number: 1.7
                                                                            Enter a real number: 4.1
                                                                            Enter a real number: 1.65
                                                                            Enter a real number: 7.32
                                                                            Enter a real number: 6.66
                                                                            Enter a real number: 4.53
                                                                            Enter a real number: 9.01
                                                                            Enter a real number: 2.15 
                                                                            Average is : 4.272

                                                                            10. Python program to display the given integer in a reverse manner

                                                                            number = int(input("Enter a positive integer: "))
                                                                            rev = 0
                                                                            while(number!=0):
                                                                                    digit = number%10
                                                                                        rev = (rev*10)+digit
                                                                                            number = number//10
                                                                                            print(rev)
                                                                                            Output:

                                                                                                Enter a positive integer: 739
                                                                                                937

                                                                                                11. Python program to find the geometric mean of n numbers
                                                                                                c = 0
                                                                                                p = 1.0
                                                                                                count = int(input("Enter the number of values: "))
                                                                                                while(c<count):
                                                                                                        x = float(input("Enter a real number: "))
                                                                                                            c = c+1
                                                                                                                p = p * x
                                                                                                                gm = pow(p,1.0/count)
                                                                                                                print("The geometric mean is: ",gm)
                                                                                                                Output:

                                                                                                                    Enter the number of values: 6
                                                                                                                    Enter a real number: 3.2
                                                                                                                    Enter a real number: 1.54
                                                                                                                    Enter a real number: 4.11
                                                                                                                    Enter a real number: 9.12
                                                                                                                    Enter a real number: 7.56
                                                                                                                    Enter a real number: 3.14
                                                                                                                    The geometric mean is:  4.045694954202098

                                                                                                                    12. Python program to find the sum of the digits of an integer using a while loop

                                                                                                                    sum = 0
                                                                                                                    number = int(input("Enter an integer: "))
                                                                                                                    while(number!=0):
                                                                                                                            digit = number%10
                                                                                                                                sum = sum+digit
                                                                                                                                    number = number//10
                                                                                                                                    print("Sum of digits is: ", sum)
                                                                                                                                    Output:

                                                                                                                                        Enter an integer: 395
                                                                                                                                        Sum of digits is:  17

                                                                                                                                        13. Python program to display all the multiples of 3 within the range 10 to 50

                                                                                                                                        for i in range(10,50):
                                                                                                                                                if (i%3==0):
                                                                                                                                                            print(i)
                                                                                                                                                            Output:
                                                                                                                                                                Ezoic

                                                                                                                                                                12
                                                                                                                                                                15
                                                                                                                                                                18
                                                                                                                                                                21
                                                                                                                                                                24
                                                                                                                                                                27
                                                                                                                                                                30
                                                                                                                                                                33
                                                                                                                                                                36
                                                                                                                                                                39
                                                                                                                                                                42
                                                                                                                                                                45
                                                                                                                                                                48

                                                                                                                                                                14. Python program to display all integers within the range 100-200 whose sum of digits is an even number

                                                                                                                                                                for i in range(100,200):
                                                                                                                                                                        num = i
                                                                                                                                                                            sum = 0
                                                                                                                                                                                while(num!=0):
                                                                                                                                                                                            digit = num%10
                                                                                                                                                                                                    sum = sum + digit
                                                                                                                                                                                                            num = num//10
                                                                                                                                                                                                                if(sum%2==0):
                                                                                                                                                                                                                            print(i)
                                                                                                                                                                                                                            Output:

                                                                                                                                                                                                                                101
                                                                                                                                                                                                                                103
                                                                                                                                                                                                                                105
                                                                                                                                                                                                                                107
                                                                                                                                                                                                                                109
                                                                                                                                                                                                                                110
                                                                                                                                                                                                                                112
                                                                                                                                                                                                                                114
                                                                                                                                                                                                                                116
                                                                                                                                                                                                                                118
                                                                                                                                                                                                                                121
                                                                                                                                                                                                                                123
                                                                                                                                                                                                                                125
                                                                                                                                                                                                                                127
                                                                                                                                                                                                                                129
                                                                                                                                                                                                                                130
                                                                                                                                                                                                                                132
                                                                                                                                                                                                                                134
                                                                                                                                                                                                                                136
                                                                                                                                                                                                                                138
                                                                                                                                                                                                                                141
                                                                                                                                                                                                                                143
                                                                                                                                                                                                                                145
                                                                                                                                                                                                                                147
                                                                                                                                                                                                                                149
                                                                                                                                                                                                                                150
                                                                                                                                                                                                                                152
                                                                                                                                                                                                                                154
                                                                                                                                                                                                                                156
                                                                                                                                                                                                                                158
                                                                                                                                                                                                                                161
                                                                                                                                                                                                                                163
                                                                                                                                                                                                                                165
                                                                                                                                                                                                                                167
                                                                                                                                                                                                                                169
                                                                                                                                                                                                                                170
                                                                                                                                                                                                                                172
                                                                                                                                                                                                                                174
                                                                                                                                                                                                                                176
                                                                                                                                                                                                                                178
                                                                                                                                                                                                                                181
                                                                                                                                                                                                                                183
                                                                                                                                                                                                                                185
                                                                                                                                                                                                                                187
                                                                                                                                                                                                                                189
                                                                                                                                                                                                                                190
                                                                                                                                                                                                                                192
                                                                                                                                                                                                                                194
                                                                                                                                                                                                                                196
                                                                                                                                                                                                                                198

                                                                                                                                                                                                                                15. Python program to check whether the given integer is a prime number or not

                                                                                                                                                                                                                                num = int(input("Enter an integer greater than 1: "))
                                                                                                                                                                                                                                isprime = 1 #assuming that num is prime
                                                                                                                                                                                                                                for i in range(2,num//2):
                                                                                                                                                                                                                                        if (num%i==0):
                                                                                                                                                                                                                                                    isprime = 0
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        if(isprime==1):
                                                                                                                                                                                                                                                                print(num, "is a prime number")
                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                    print(num, "is not a prime number")
                                                                                                                                                                                                                                                                    Output:

                                                                                                                                                                                                                                                                        Enter an integer greater than 1: 7
                                                                                                                                                                                                                                                                        7 is a prime number
                                                                                                                                                                                                                                                                        Enter an integer greater than 1: 24
                                                                                                                                                                                                                                                                        24 is not a prime number

                                                                                                                                                                                                                                                                        16. Python program to generate the prime numbers from 1 to N

                                                                                                                                                                                                                                                                        num =int(input("Enter the range: "))
                                                                                                                                                                                                                                                                        for n in range(2,num):
                                                                                                                                                                                                                                                                                for i in range(2,n):
                                                                                                                                                                                                                                                                                            if(n%i==0):
                                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                        print(n)   
                                                                                                                                                                                                                                                                                                                        Output:

                                                                                                                                                                                                                                                                                                                            Enter the range: 6
                                                                                                                                                                                                                                                                                                                            2
                                                                                                                                                                                                                                                                                                                            3
                                                                                                                                                                                                                                                                                                                            5

                                                                                                                                                                                                                                                                                                                            17. Python program to find the roots of a quadratic equation

                                                                                                                                                                                                                                                                                                                            import math
                                                                                                                                                                                                                                                                                                                            a = float(input("Enter the first coefficient: "))
                                                                                                                                                                                                                                                                                                                            b = float(input("Enter the second coefficient: "))
                                                                                                                                                                                                                                                                                                                            c = float(input("Enter the third coefficient: "))
                                                                                                                                                                                                                                                                                                                            if (a!=0.0):
                                                                                                                                                                                                                                                                                                                                    d = (b*b)-(4*a*c) 
                                                                                                                                                                                                                                                                                                                                        if (d==0.0):
                                                                                                                                                                                                                                                                                                                                                    print("The roots are real and equal.") 
                                                                                                                                                                                                                                                                                                                                                            r = -b/(2*a)
                                                                                                                                                                                                                                                                                                                                                                    print("The roots are ", r,"and", r)
                                                                                                                                                                                                                                                                                                                                                                        elif(d>0.0):
                                                                                                                                                                                                                                                                                                                                                                                    print("The roots are real and distinct.")
                                                                                                                                                                                                                                                                                                                                                                                            r1 = (-b+(math.sqrt(d)))/(2*a) 
                                                                                                                                                                                                                                                                                                                                                                                                    r2 = (-b-(math.sqrt(d)))/(2*a)
                                                                                                                                                                                                                                                                                                                                                                                                            print("The root1 is: ", r1)
                                                                                                                                                                                                                                                                                                                                                                                                                    print("The root2 is: ", r2)
                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                    print("The roots are imaginary.")
                                                                                                                                                                                                                                                                                                                                                                                                                                            rp = -b/(2*a)
                                                                                                                                                                                                                                                                                                                                                                                                                                                    ip = math.sqrt(-d)/(2*a)
                                                                                                                                                                                                                                                                                                                                                                                                                                                            print("The root1 is: ", rp, "+ i",ip)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print("The root2 is: ", rp, "- i",ip)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("Not a quadratic equation.")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Enter the first coefficient: 4
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Enter the second coefficient: 7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Enter the third coefficient: 2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            The roots are real and distinct.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            The root1 is:  -0.3596117967977924
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            The root2 is:  -1.3903882032022077

                                                                                                                                                                                                                                                                                                                                                                                                                                                                            18. Python program to print the numbers from a given number n till 0 using recursion

                                                                                                                                                                                                                                                                                                                                                                                                                                                                            def print_till_zero(n):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if (n==0):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                return
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(n)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    n=n-1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print_till_zero(n)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print_till_zero(8)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            8
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            6
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            4
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            3
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            1

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            19. Python program to find the factorial of a number using recursion

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            def fact(n):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if n==1:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                f=1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                f = n * fact(n-1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    return f
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                num = int(input("Enter an integer: "))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                result = fact(num)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("The factorial of", num, " is: ", result)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Enter an integer: 5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The factorial of 5  is:  120

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    20. Python program to display the sum of n numbers using a list

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    numbers = []
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    num = int(input('How many numbers: '))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    for n in range(num):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            x = int(input('Enter number '))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                numbers.append(x)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("Sum of numbers in the given list is :", sum(numbers))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    How many numbers: 3
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Enter number 2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Enter number 3
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Enter number 4
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Sum of numbers in the given list is : 9

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    21. Python program to implement linear search

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    numbers = [4,2,7,1,8,3,6]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    f = 0 #flag
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    x = int(input("Enter the number to be found out: "))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    for i in range(len(numbers)):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if (x==numbers[i]):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("Successful search, the element is found at position", i)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                f = 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if(f==0):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print("Oops! Search unsuccessful")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Enter the number to be found out: 7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Successful search, the element is found at position 2

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                22. Python program to implement binary search

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def binarySearch(numbers, low, high, x):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if (high >= low):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    mid = low + (high - low)//2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if (numbers[mid] == x):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            return mid
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                elif (numbers[mid] > x):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                return binarySearch(numbers, low, mid-1, x)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    return binarySearch(numbers, mid+1, high, x)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                return -1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            numbers = [ 1,4,6,7,12,17,25 ]   #binary search requires sorted numbers
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            x = 7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            result = binarySearch(numbers, 0, len(numbers)-1, x)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if (result != -1):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print("Search successful, element found at position ", result)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("The given element is not present in the array")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Search successful, element found at position  3

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            23. Python program to find the odd numbers in an array

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            numbers = [8,3,1,6,2,4,5,9]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            count = 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            for i in range(len(numbers)):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if(numbers[i]%2!=0):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                count = count+1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("The number of odd numbers in the list are: ", count)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The number of odd numbers in the list are:  4

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    24. Python program to find the largest number in a list without using built-in functions

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    numbers = [3,8,1,7,2,9,5,4]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    big = numbers[0]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    position = 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    for i in range(len(numbers)):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if (numbers[i]>big):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        big = numbers[i]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                position = i
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("The largest element is ",big," which is found at position ",position)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The largest element is  9  which is found at position  5

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    25. Python program to insert a number to any position in a list

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    numbers = [3,4,1,9,6,2,8]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print(numbers)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    x = int(input("Enter the number to be inserted: "))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    y = int(input("Enter the position: "))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    numbers.insert(y,x)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print(numbers)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        [3, 4, 1, 9, 6, 2, 8]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Enter the number to be inserted: 11
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Enter the position: 2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        [3, 4, 11, 1, 9, 6, 2, 8]

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        26. Python program to delete an element from a list by index

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        numbers = [3,4,1,9,6,2,8]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print(numbers)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        x = int(input("Enter the position of the element to be deleted: "))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        numbers.pop(x)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print(numbers)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [3, 4, 1, 9, 6, 2, 8]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Enter the position of the element to be deleted: 4
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [3, 4, 1, 9, 2, 8]

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            27. Python program to check whether a string is palindrome or not

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            def rev(inputString):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    return inputString[::-1]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def isPalindrome(inputString):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        reverseString = rev(inputString)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if (inputString == reverseString):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        return True
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        return False
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    s = input("Enter a string: ")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    result = isPalindrome(s)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if result == 1:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print("The string is palindrome")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("The string is not palindrome")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Enter a string: malayalam
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The string is palindrome
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Enter a string: car
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The string is not palindrome

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    28. Python program to implement matrix addition

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    X = [[8,5,1],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [9 ,3,2],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [4 ,6,3]]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Y = [[8,5,3],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [9,5,7],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [9,4,1]]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    result = [[0,0,0],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [0,0,0],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [0,0,0]]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    for i in range(len(X)):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            for j in range(len(X[0])):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        result[i][j] = X[i][j] + Y[i][j]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        for k in result:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(k)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    [16, 10, 4]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    [18, 8, 9]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    [13, 10, 4]

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    29. Python program to implement matrix multiplication

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    X = [[8,5,1],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [9 ,3,2],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [4 ,6,3]]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Y = [[8,5,3],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [9,5,7],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [9,4,1]]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    result = [[0,0,0,0],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [0,0,0,0],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            [0,0,0,0]]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    for i in range(len(X)):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            for j in range(len(Y[0])):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        for k in range(len(Y)):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        result[i][j] += X[i][k] * Y[k][j]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        for x in result:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(x)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Ezoic

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    [118, 69, 60, 0]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    [117, 68, 50, 0]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    [113, 62, 57, 0]

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    30. Python program to check leap year

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    year = int(input("Enter a year: "))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if (year % 4) == 0:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if (year % 100) == 0:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if (year % 400) == 0:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print(year, "is a leap year")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(year, "is not a leap year")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(year, "is a leap year")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print(year, " is not a leap year")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Enter a year: 2023
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        2023 is not a leap year
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Enter a year: 2024
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        2024 is a leap year

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        31. Python program to find the Nth term in a Fibonacci series using recursion

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        def Fib(n):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if n<0:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print("The input is incorrect.")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                elif n==1:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            return 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            elif n==2:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        return 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    return Fib(n-1)+Fib(n-2)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(Fib(7))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    8

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    32. Python program to print Fibonacci series using iteration

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    a = 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    b = 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    n=int(input("Enter the number of terms in the sequence: "))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print(a,b,end=" ")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    while(n-2):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            c=a+b
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                a,b = b,c
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print(c,end=" ")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        n=n-1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Enter the number of terms in the sequence: 8
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            0 1 1 2 3 5 8 13

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            33. Python program to print all the items in a dictionary
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            phone_book = {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'John' : [ '8592970000', 'john@xyzmail.com' ],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'Bob': [ '7994880000', 'bob@xyzmail.com' ],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            for k,v in phone_book.items():
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print(k, ":", v)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        John : ['8592970000', 'john@xyzmail.com']
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Bob : ['7994880000', 'bob@xyzmail.com']
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Tom : ['9749552647', 'tom@xyzmail.com']

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        34. Python program to implement a calculator to do basic operations

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        def add(x,y):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(x+y)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def subtract(x,y):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print(x-y)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        def multiply(x,y):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(x*y)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def divide(x,y):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print(x/y)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("Enter two numbers")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        n1=input()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        n2=input()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("Enter the operation +,-,*,/ ") 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        op=input() 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if op=='+':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                add(int(n1),int(n2))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            elif op=='-':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    subtract(int(n1),int(n2))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                elif op=='*':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        multiply(int(n1),int(n2))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    elif op=='/':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            divide(int(n1),int(n2))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(" Invalid entry ")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Ezoic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    6
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Enter the operation +,-,*,/ 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    30

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    35. Python program to draw a circle of squares using Turtle
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    import turtle
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    x=turtle.Turtle()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    def square(angle):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            x.forward(100)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                x.right(angle)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    x.forward(100)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        x.right(angle)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            x.forward(100)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                x.right(angle)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    x.forward(100)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        x.right(angle+10)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        for i in range(36):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                square(90)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Output:1. Python program to check whether the given number is even or not.

number = input("Enter a number: ")
x = int(number)%2
if x == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
Output:

Enter a number: 7
The number is Odd.
Enter a number: 6
The number is Even.

2. Python program to convert the temperature in degree centigrade to Fahrenheit

c = input("Enter temperature in Centigrade: ")
f = (9*(int(c))/5)+32
print("Temperature in Fahrenheit is: ", f)
Output:

Enter temperature in Centigrade: 30
Temperature in Fahrenheit is:  86.0

3. Python program to find the area of a triangle whose sides are given

import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ", area)
Output:

Enter the length of side a: 4.0
Enter the length of side b: 3.0
Enter the length of side c: 6.0
Area of the triangle is:  5.332682251925386

4. Python program to find out the average of a set of integers

count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print("The average is: ", avg)
Output:

Enter the count of numbers: 5
Enter an integer: 3
Enter an integer: 6
Enter an integer: 8
Enter an integer: 5
Enter an integer: 7
The average is:  5.8

5. Python program to find the product of a set of real numbers

i = 0
product = 1
count = int(input("Enter the number of real numbers: "))
for i in range(count):
    x = float(input("Enter a real number: "))
    product = product * x
print("The product of the numbers is: ", product)
Ezoic
Output:

Enter the number of real numbers: 4
Enter a real number: 3.2
Enter a real number: 2.9
Enter a real number: 7.4
Enter a real number: 5.5
The product of the numbers is:  377.69599999999997

6. Python program to find the circumference and area of a circle with a given radius

import math
r = float(input("Input the radius of the circle: "))
c = 2 * math.pi * r
area = math.pi * r * r
print("The circumference of the circle is: ", c)
print("The area of the circle is: ", area)
Output:

Input the radius of the circle: 4.3
The circumference of the circle is:  27.01769682087222
The area of the circle is:  58.088048164875275

7. Python program to check whether the given integer is a multiple of 5

number = int(input("Enter an integer: "))
if(number%5==0):
    print(number, "is a multile of 5")
else:
    print(number, "is not a multiple of 5")
Output:

Enter an integer: 23
23 is not a multiple of 5
Enter an integer: 55
55 is a multile of 5

8. Python program to check whether the given integer is a multiple of both 5 and 7

number = int(input("Enter an integer: "))
if((number%5==0)and(number%7==0)):
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of both 5 and 7")

Ezoic
Output:

Enter an integer: 33
33 is not a multiple of both 5 and 7
Enter an integer: 35
35 is a multiple of both 5 and 7

9. Python program to find the average of 10 numbers using while loop

count = 0
sum = 0.0
while(count<10):
    number = float(input("Enter a real number: "))
    count=count+1
    sum = sum+number
avg = sum/10
print("Average is :",avg)
Output:

Enter a real number: 2.3
Enter a real number: 3.3
Enter a real number: 1.7
Enter a real number: 4.1
Enter a real number: 1.65
Enter a real number: 7.32
Enter a real number: 6.66
Enter a real number: 4.53
Enter a real number: 9.01
Enter a real number: 2.15 
Average is : 4.272

10. Python program to display the given integer in a reverse manner

number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    rev = (rev*10)+digit
    number = number//10
print(rev)
Output:

Enter a positive integer: 739
937

11. Python program to find the geometric mean of n numbers
c = 0
p = 1.0
count = int(input("Enter the number of values: "))
while(c<count):
    x = float(input("Enter a real number: "))
    c = c+1
    p = p * x
gm = pow(p,1.0/count)
print("The geometric mean is: ",gm)
Output:

Enter the number of values: 6
Enter a real number: 3.2
Enter a real number: 1.54
Enter a real number: 4.11
Enter a real number: 9.12
Enter a real number: 7.56
Enter a real number: 3.14
The geometric mean is:  4.045694954202098

12. Python program to find the sum of the digits of an integer using a while loop

sum = 0
number = int(input("Enter an integer: "))
while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digits is: ", sum)
Output:

Enter an integer: 395
Sum of digits is:  17

13. Python program to display all the multiples of 3 within the range 10 to 50

for i in range(10,50):
    if (i%3==0):
        print(i)
Output:
Ezoic

12
15
18
21
24
27
30
33
36
39
42
45
48

14. Python program to display all integers within the range 100-200 whose sum of digits is an even number

for i in range(100,200):
    num = i
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    if(sum%2==0):
        print(i)
Output:

101
103
105
107
109
110
112
114
116
118
121
123
125
127
129
130
132
134
136
138
141
143
145
147
149
150
152
154
156
158
161
163
165
167
169
170
172
174
176
178
181
183
185
187
189
190
192
194
196
198

15. Python program to check whether the given integer is a prime number or not

num = int(input("Enter an integer greater than 1: "))
isprime = 1 #assuming that num is prime
for i in range(2,num//2):
    if (num%i==0):
        isprime = 0
        break
if(isprime==1):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
Output:

Enter an integer greater than 1: 7
7 is a prime number
Enter an integer greater than 1: 24
24 is not a prime number

16. Python program to generate the prime numbers from 1 to N

num =int(input("Enter the range: "))
for n in range(2,num):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)   
Output:

Enter the range: 6
2
3
5

17. Python program to find the roots of a quadratic equation

import math
a = float(input("Enter the first coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the third coefficient: "))
if (a!=0.0):
    d = (b*b)-(4*a*c) 
    if (d==0.0):
        print("The roots are real and equal.") 
        r = -b/(2*a)
        print("The roots are ", r,"and", r)
    elif(d>0.0):
        print("The roots are real and distinct.")
        r1 = (-b+(math.sqrt(d)))/(2*a) 
        r2 = (-b-(math.sqrt(d)))/(2*a)
        print("The root1 is: ", r1)
        print("The root2 is: ", r2)
    else:
        print("The roots are imaginary.")
        rp = -b/(2*a)
        ip = math.sqrt(-d)/(2*a)
        print("The root1 is: ", rp, "+ i",ip)
        print("The root2 is: ", rp, "- i",ip)
else:
    print("Not a quadratic equation.")
Output:

Ezoic
Enter the first coefficient: 4
Enter the second coefficient: 7
Enter the third coefficient: 2
The roots are real and distinct.
The root1 is:  -0.3596117967977924
The root2 is:  -1.3903882032022077

18. Python program to print the numbers from a given number n till 0 using recursion

def print_till_zero(n):
    if (n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
print_till_zero(8)
Output:

Ezoic
8
7
6
5
4
3
2
1

19. Python program to find the factorial of a number using recursion

def fact(n):
    if n==1:
        f=1
    else:
        f = n * fact(n-1)
    return f
num = int(input("Enter an integer: "))
result = fact(num)
print("The factorial of", num, " is: ", result)
Output:

Enter an integer: 5
The factorial of 5  is:  120

20. Python program to display the sum of n numbers using a list

numbers = []
num = int(input('How many numbers: '))
for n in range(num):
    x = int(input('Enter number '))
    numbers.append(x)
print("Sum of numbers in the given list is :", sum(numbers))
Output:

How many numbers: 3
Enter number 2
Enter number 3
Enter number 4
Sum of numbers in the given list is : 9

21. Python program to implement linear search

numbers = [4,2,7,1,8,3,6]
f = 0 #flag
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
    if (x==numbers[i]):
        print("Successful search, the element is found at position", i)
        f = 1
        break
if(f==0):
    print("Oops! Search unsuccessful")
Output:

Enter the number to be found out: 7
Successful search, the element is found at position 2

22. Python program to implement binary search

def binarySearch(numbers, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if (numbers[mid] == x):
            return mid
        elif (numbers[mid] > x):
            return binarySearch(numbers, low, mid-1, x)
        else:
            return binarySearch(numbers, mid+1, high, x)
    else:
        return -1
numbers = [ 1,4,6,7,12,17,25 ]   #binary search requires sorted numbers
x = 7
result = binarySearch(numbers, 0, len(numbers)-1, x)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")
Output:

Ezoic
Search successful, element found at position  3

23. Python program to find the odd numbers in an array

numbers = [8,3,1,6,2,4,5,9]
count = 0
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        count = count+1
print("The number of odd numbers in the list are: ", count)
Ezoic
Output:

The number of odd numbers in the list are:  4

24. Python program to find the largest number in a list without using built-in functions

numbers = [3,8,1,7,2,9,5,4]
big = numbers[0]
position = 0
for i in range(len(numbers)):
    if (numbers[i]>big):
        big = numbers[i]
        position = i
print("The largest element is ",big," which is found at position ",position)
Output:

Ezoic
The largest element is  9  which is found at position  5

25. Python program to insert a number to any position in a list

numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the number to be inserted: "))
y = int(input("Enter the position: "))
numbers.insert(y,x)
print(numbers)
Output:

[3, 4, 1, 9, 6, 2, 8]
Enter the number to be inserted: 11
Enter the position: 2
[3, 4, 11, 1, 9, 6, 2, 8]

26. Python program to delete an element from a list by index

numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the position of the element to be deleted: "))
numbers.pop(x)
print(numbers)
Ezoic
Output:

Ezoic
[3, 4, 1, 9, 6, 2, 8]
Enter the position of the element to be deleted: 4
[3, 4, 1, 9, 2, 8]

27. Python program to check whether a string is palindrome or not

def rev(inputString):
    return inputString[::-1]
def isPalindrome(inputString):
    reverseString = rev(inputString)
    if (inputString == reverseString):
        return True
    return False
s = input("Enter a string: ")
result = isPalindrome(s)
if result == 1:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
Output:

Enter a string: malayalam
The string is palindrome
Enter a string: car
The string is not palindrome

28. Python program to implement matrix addition

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for k in result:
    print(k)
Output:

Ezoic
[16, 10, 4]
[18, 8, 9]
[13, 10, 4]

29. Python program to implement matrix multiplication

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for x in result:
    print(x)
Output:
Ezoic

Ezoic
[118, 69, 60, 0]
[117, 68, 50, 0]
[113, 62, 57, 0]

30. Python program to check leap year

year = int(input("Enter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, " is not a leap year")
Output:

Enter a year: 2023
2023 is not a leap year
Enter a year: 2024
2024 is a leap year

31. Python program to find the Nth term in a Fibonacci series using recursion

def Fib(n):
    if n<0:
        print("The input is incorrect.")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(7))
Output:

Ezoic
8

32. Python program to print Fibonacci series using iteration

a = 0
b = 1
n=int(input("Enter the number of terms in the sequence: "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a,b = b,c
    print(c,end=" ")
    n=n-1
Output:

Enter the number of terms in the sequence: 8
0 1 1 2 3 5 8 13

33. Python program to print all the items in a dictionary
phone_book = {
'John' : [ '8592970000', 'john@xyzmail.com' ],
'Bob': [ '7994880000', 'bob@xyzmail.com' ],
'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
}
for k,v in phone_book.items():
    print(k, ":", v)
Output:

Ezoic
John : ['8592970000', 'john@xyzmail.com']
Bob : ['7994880000', 'bob@xyzmail.com']
Tom : ['9749552647', 'tom@xyzmail.com']

34. Python program to implement a calculator to do basic operations

def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
print("Enter two numbers")
n1=input()
n2=input()
print("Enter the operation +,-,*,/ ") 
op=input() 
if op=='+':
    add(int(n1),int(n2))
elif op=='-':
    subtract(int(n1),int(n2))
elif op=='*':
    multiply(int(n1),int(n2))
elif op=='/':
    divide(int(n1),int(n2))
else:
    print(" Invalid entry ")
Output:

Ezoic
5
6
Enter the operation +,-,*,/ 
*
30

35. Python program to draw a circle of squares using Turtle
import turtle
x=turtle.Turtle()


def square(angle):
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle+10)

for i in range(36):
    square(90)
Output:1. Python program to check whether the given number is even or not.

number = input("Enter a number: ")
x = int(number)%2
if x == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
Output:

Enter a number: 7
The number is Odd.
Enter a number: 6
The number is Even.

2. Python program to convert the temperature in degree centigrade to Fahrenheit

c = input("Enter temperature in Centigrade: ")
f = (9*(int(c))/5)+32
print("Temperature in Fahrenheit is: ", f)
Output:

Enter temperature in Centigrade: 30
Temperature in Fahrenheit is:  86.0

3. Python program to find the area of a triangle whose sides are given

import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ", area)
Output:

Enter the length of side a: 4.0
Enter the length of side b: 3.0
Enter the length of side c: 6.0
Area of the triangle is:  5.332682251925386

4. Python program to find out the average of a set of integers

count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print("The average is: ", avg)
Output:

Enter the count of numbers: 5
Enter an integer: 3
Enter an integer: 6
Enter an integer: 8
Enter an integer: 5
Enter an integer: 7
The average is:  5.8

5. Python program to find the product of a set of real numbers

i = 0
product = 1
count = int(input("Enter the number of real numbers: "))
for i in range(count):
    x = float(input("Enter a real number: "))
    product = product * x
print("The product of the numbers is: ", product)
Ezoic
Output:

Enter the number of real numbers: 4
Enter a real number: 3.2
Enter a real number: 2.9
Enter a real number: 7.4
Enter a real number: 5.5
The product of the numbers is:  377.69599999999997

6. Python program to find the circumference and area of a circle with a given radius

import math
r = float(input("Input the radius of the circle: "))
c = 2 * math.pi * r
area = math.pi * r * r
print("The circumference of the circle is: ", c)
print("The area of the circle is: ", area)
Output:

Input the radius of the circle: 4.3
The circumference of the circle is:  27.01769682087222
The area of the circle is:  58.088048164875275

7. Python program to check whether the given integer is a multiple of 5

number = int(input("Enter an integer: "))
if(number%5==0):
    print(number, "is a multile of 5")
else:
    print(number, "is not a multiple of 5")
Output:

Enter an integer: 23
23 is not a multiple of 5
Enter an integer: 55
55 is a multile of 5

8. Python program to check whether the given integer is a multiple of both 5 and 7

number = int(input("Enter an integer: "))
if((number%5==0)and(number%7==0)):
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of both 5 and 7")

Ezoic
Output:

Enter an integer: 33
33 is not a multiple of both 5 and 7
Enter an integer: 35
35 is a multiple of both 5 and 7

9. Python program to find the average of 10 numbers using while loop

count = 0
sum = 0.0
while(count<10):
    number = float(input("Enter a real number: "))
    count=count+1
    sum = sum+number
avg = sum/10
print("Average is :",avg)
Output:

Enter a real number: 2.3
Enter a real number: 3.3
Enter a real number: 1.7
Enter a real number: 4.1
Enter a real number: 1.65
Enter a real number: 7.32
Enter a real number: 6.66
Enter a real number: 4.53
Enter a real number: 9.01
Enter a real number: 2.15 
Average is : 4.272

10. Python program to display the given integer in a reverse manner

number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    rev = (rev*10)+digit
    number = number//10
print(rev)
Output:

Enter a positive integer: 739
937

11. Python program to find the geometric mean of n numbers
c = 0
p = 1.0
count = int(input("Enter the number of values: "))
while(c<count):
    x = float(input("Enter a real number: "))
    c = c+1
    p = p * x
gm = pow(p,1.0/count)
print("The geometric mean is: ",gm)
Output:

Enter the number of values: 6
Enter a real number: 3.2
Enter a real number: 1.54
Enter a real number: 4.11
Enter a real number: 9.12
Enter a real number: 7.56
Enter a real number: 3.14
The geometric mean is:  4.045694954202098

12. Python program to find the sum of the digits of an integer using a while loop

sum = 0
number = int(input("Enter an integer: "))
while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digits is: ", sum)
Output:

Enter an integer: 395
Sum of digits is:  17

13. Python program to display all the multiples of 3 within the range 10 to 50

for i in range(10,50):
    if (i%3==0):
        print(i)
Output:
Ezoic

12
15
18
21
24
27
30
33
36
39
42
45
48

14. Python program to display all integers within the range 100-200 whose sum of digits is an even number

for i in range(100,200):
    num = i
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    if(sum%2==0):
        print(i)
Output:

101
103
105
107
109
110
112
114
116
118
121
123
125
127
129
130
132
134
136
138
141
143
145
147
149
150
152
154
156
158
161
163
165
167
169
170
172
174
176
178
181
183
185
187
189
190
192
194
196
198

15. Python program to check whether the given integer is a prime number or not

num = int(input("Enter an integer greater than 1: "))
isprime = 1 #assuming that num is prime
for i in range(2,num//2):
    if (num%i==0):
        isprime = 0
        break
if(isprime==1):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
Output:

Enter an integer greater than 1: 7
7 is a prime number
Enter an integer greater than 1: 24
24 is not a prime number

16. Python program to generate the prime numbers from 1 to N

num =int(input("Enter the range: "))
for n in range(2,num):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)   
Output:

Enter the range: 6
2
3
5

17. Python program to find the roots of a quadratic equation

import math
a = float(input("Enter the first coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the third coefficient: "))
if (a!=0.0):
    d = (b*b)-(4*a*c) 
    if (d==0.0):
        print("The roots are real and equal.") 
        r = -b/(2*a)
        print("The roots are ", r,"and", r)
    elif(d>0.0):
        print("The roots are real and distinct.")
        r1 = (-b+(math.sqrt(d)))/(2*a) 
        r2 = (-b-(math.sqrt(d)))/(2*a)
        print("The root1 is: ", r1)
        print("The root2 is: ", r2)
    else:
        print("The roots are imaginary.")
        rp = -b/(2*a)
        ip = math.sqrt(-d)/(2*a)
        print("The root1 is: ", rp, "+ i",ip)
        print("The root2 is: ", rp, "- i",ip)
else:
    print("Not a quadratic equation.")
Output:

Ezoic
Enter the first coefficient: 4
Enter the second coefficient: 7
Enter the third coefficient: 2
The roots are real and distinct.
The root1 is:  -0.3596117967977924
The root2 is:  -1.3903882032022077

18. Python program to print the numbers from a given number n till 0 using recursion

def print_till_zero(n):
    if (n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
print_till_zero(8)
Output:

Ezoic
8
7
6
5
4
3
2
1

19. Python program to find the factorial of a number using recursion

def fact(n):
    if n==1:
        f=1
    else:
        f = n * fact(n-1)
    return f
num = int(input("Enter an integer: "))
result = fact(num)
print("The factorial of", num, " is: ", result)
Output:

Enter an integer: 5
The factorial of 5  is:  120

20. Python program to display the sum of n numbers using a list

numbers = []
num = int(input('How many numbers: '))
for n in range(num):
    x = int(input('Enter number '))
    numbers.append(x)
print("Sum of numbers in the given list is :", sum(numbers))
Output:

How many numbers: 3
Enter number 2
Enter number 3
Enter number 4
Sum of numbers in the given list is : 9

21. Python program to implement linear search

numbers = [4,2,7,1,8,3,6]
f = 0 #flag
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
    if (x==numbers[i]):
        print("Successful search, the element is found at position", i)
        f = 1
        break
if(f==0):
    print("Oops! Search unsuccessful")
Output:

Enter the number to be found out: 7
Successful search, the element is found at position 2

22. Python program to implement binary search

def binarySearch(numbers, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if (numbers[mid] == x):
            return mid
        elif (numbers[mid] > x):
            return binarySearch(numbers, low, mid-1, x)
        else:
            return binarySearch(numbers, mid+1, high, x)
    else:
        return -1
numbers = [ 1,4,6,7,12,17,25 ]   #binary search requires sorted numbers
x = 7
result = binarySearch(numbers, 0, len(numbers)-1, x)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")
Output:

Ezoic
Search successful, element found at position  3

23. Python program to find the odd numbers in an array

numbers = [8,3,1,6,2,4,5,9]
count = 0
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        count = count+1
print("The number of odd numbers in the list are: ", count)
Ezoic
Output:

The number of odd numbers in the list are:  4

24. Python program to find the largest number in a list without using built-in functions

numbers = [3,8,1,7,2,9,5,4]
big = numbers[0]
position = 0
for i in range(len(numbers)):
    if (numbers[i]>big):
        big = numbers[i]
        position = i
print("The largest element is ",big," which is found at position ",position)
Output:

Ezoic
The largest element is  9  which is found at position  5

25. Python program to insert a number to any position in a list

numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the number to be inserted: "))
y = int(input("Enter the position: "))
numbers.insert(y,x)
print(numbers)
Output:

[3, 4, 1, 9, 6, 2, 8]
Enter the number to be inserted: 11
Enter the position: 2
[3, 4, 11, 1, 9, 6, 2, 8]

26. Python program to delete an element from a list by index

numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the position of the element to be deleted: "))
numbers.pop(x)
print(numbers)
Ezoic
Output:

Ezoic
[3, 4, 1, 9, 6, 2, 8]
Enter the position of the element to be deleted: 4
[3, 4, 1, 9, 2, 8]

27. Python program to check whether a string is palindrome or not

def rev(inputString):
    return inputString[::-1]
def isPalindrome(inputString):
    reverseString = rev(inputString)
    if (inputString == reverseString):
        return True
    return False
s = input("Enter a string: ")
result = isPalindrome(s)
if result == 1:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
Output:

Enter a string: malayalam
The string is palindrome
Enter a string: car
The string is not palindrome

28. Python program to implement matrix addition

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for k in result:
    print(k)
Output:

Ezoic
[16, 10, 4]
[18, 8, 9]
[13, 10, 4]

29. Python program to implement matrix multiplication

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for x in result:
    print(x)
Output:
Ezoic

Ezoic
[118, 69, 60, 0]
[117, 68, 50, 0]
[113, 62, 57, 0]

30. Python program to check leap year

year = int(input("Enter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, " is not a leap year")
Output:

Enter a year: 2023
2023 is not a leap year
Enter a year: 2024
2024 is a leap year

31. Python program to find the Nth term in a Fibonacci series using recursion

def Fib(n):
    if n<0:
        print("The input is incorrect.")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(7))
Output:

Ezoic
8

32. Python program to print Fibonacci series using iteration

a = 0
b = 1
n=int(input("Enter the number of terms in the sequence: "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a,b = b,c
    print(c,end=" ")
    n=n-1
Output:

Enter the number of terms in the sequence: 8
0 1 1 2 3 5 8 13

33. Python program to print all the items in a dictionary
phone_book = {
'John' : [ '8592970000', 'john@xyzmail.com' ],
'Bob': [ '7994880000', 'bob@xyzmail.com' ],
'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
}
for k,v in phone_book.items():
    print(k, ":", v)
Output:

Ezoic
John : ['8592970000', 'john@xyzmail.com']
Bob : ['7994880000', 'bob@xyzmail.com']
Tom : ['9749552647', 'tom@xyzmail.com']

34. Python program to implement a calculator to do basic operations

def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
print("Enter two numbers")
n1=input()
n2=input()
print("Enter the operation +,-,*,/ ") 
op=input() 
if op=='+':
    add(int(n1),int(n2))
elif op=='-':
    subtract(int(n1),int(n2))
elif op=='*':
    multiply(int(n1),int(n2))
elif op=='/':
    divide(int(n1),int(n2))
else:
    print(" Invalid entry ")
Output:

Ezoic
5
6
Enter the operation +,-,*,/ 
*
30

35. Python program to draw a circle of squares using Turtle
import turtle
x=turtle.Turtle()


def square(angle):
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle+10)

for i in range(36):
    square(90)
Output:1. Python program to check whether the given number is even or not.

number = input("Enter a number: ")
x = int(number)%2
if x == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
Output:

Enter a number: 7
The number is Odd.
Enter a number: 6
The number is Even.

2. Python program to convert the temperature in degree centigrade to Fahrenheit

c = input("Enter temperature in Centigrade: ")
f = (9*(int(c))/5)+32
print("Temperature in Fahrenheit is: ", f)
Output:

Enter temperature in Centigrade: 30
Temperature in Fahrenheit is:  86.0

3. Python program to find the area of a triangle whose sides are given

import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ", area)
Output:

Enter the length of side a: 4.0
Enter the length of side b: 3.0
Enter the length of side c: 6.0
Area of the triangle is:  5.332682251925386

4. Python program to find out the average of a set of integers

count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print("The average is: ", avg)
Output:

Enter the count of numbers: 5
Enter an integer: 3
Enter an integer: 6
Enter an integer: 8
Enter an integer: 5
Enter an integer: 7
The average is:  5.8

5. Python program to find the product of a set of real numbers

i = 0
product = 1
count = int(input("Enter the number of real numbers: "))
for i in range(count):
    x = float(input("Enter a real number: "))
    product = product * x
print("The product of the numbers is: ", product)
Ezoic
Output:

Enter the number of real numbers: 4
Enter a real number: 3.2
Enter a real number: 2.9
Enter a real number: 7.4
Enter a real number: 5.5
The product of the numbers is:  377.69599999999997

6. Python program to find the circumference and area of a circle with a given radius

import math
r = float(input("Input the radius of the circle: "))
c = 2 * math.pi * r
area = math.pi * r * r
print("The circumference of the circle is: ", c)
print("The area of the circle is: ", area)
Output:

Input the radius of the circle: 4.3
The circumference of the circle is:  27.01769682087222
The area of the circle is:  58.088048164875275

7. Python program to check whether the given integer is a multiple of 5

number = int(input("Enter an integer: "))
if(number%5==0):
    print(number, "is a multile of 5")
else:
    print(number, "is not a multiple of 5")
Output:

Enter an integer: 23
23 is not a multiple of 5
Enter an integer: 55
55 is a multile of 5

8. Python program to check whether the given integer is a multiple of both 5 and 7

number = int(input("Enter an integer: "))
if((number%5==0)and(number%7==0)):
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of both 5 and 7")

Ezoic
Output:

Enter an integer: 33
33 is not a multiple of both 5 and 7
Enter an integer: 35
35 is a multiple of both 5 and 7

9. Python program to find the average of 10 numbers using while loop

count = 0
sum = 0.0
while(count<10):
    number = float(input("Enter a real number: "))
    count=count+1
    sum = sum+number
avg = sum/10
print("Average is :",avg)
Output:

Enter a real number: 2.3
Enter a real number: 3.3
Enter a real number: 1.7
Enter a real number: 4.1
Enter a real number: 1.65
Enter a real number: 7.32
Enter a real number: 6.66
Enter a real number: 4.53
Enter a real number: 9.01
Enter a real number: 2.15 
Average is : 4.272

10. Python program to display the given integer in a reverse manner

number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    rev = (rev*10)+digit
    number = number//10
print(rev)
Output:

Enter a positive integer: 739
937

11. Python program to find the geometric mean of n numbers
c = 0
p = 1.0
count = int(input("Enter the number of values: "))
while(c<count):
    x = float(input("Enter a real number: "))
    c = c+1
    p = p * x
gm = pow(p,1.0/count)
print("The geometric mean is: ",gm)
Output:

Enter the number of values: 6
Enter a real number: 3.2
Enter a real number: 1.54
Enter a real number: 4.11
Enter a real number: 9.12
Enter a real number: 7.56
Enter a real number: 3.14
The geometric mean is:  4.045694954202098

12. Python program to find the sum of the digits of an integer using a while loop

sum = 0
number = int(input("Enter an integer: "))
while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digits is: ", sum)
Output:

Enter an integer: 395
Sum of digits is:  17

13. Python program to display all the multiples of 3 within the range 10 to 50

for i in range(10,50):
    if (i%3==0):
        print(i)
Output:
Ezoic

12
15
18
21
24
27
30
33
36
39
42
45
48

14. Python program to display all integers within the range 100-200 whose sum of digits is an even number

for i in range(100,200):
    num = i
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    if(sum%2==0):
        print(i)
Output:

101
103
105
107
109
110
112
114
116
118
121
123
125
127
129
130
132
134
136
138
141
143
145
147
149
150
152
154
156
158
161
163
165
167
169
170
172
174
176
178
181
183
185
187
189
190
192
194
196
198

15. Python program to check whether the given integer is a prime number or not

num = int(input("Enter an integer greater than 1: "))
isprime = 1 #assuming that num is prime
for i in range(2,num//2):
    if (num%i==0):
        isprime = 0
        break
if(isprime==1):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
Output:

Enter an integer greater than 1: 7
7 is a prime number
Enter an integer greater than 1: 24
24 is not a prime number

16. Python program to generate the prime numbers from 1 to N

num =int(input("Enter the range: "))
for n in range(2,num):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)   
Output:

Enter the range: 6
2
3
5

17. Python program to find the roots of a quadratic equation

import math
a = float(input("Enter the first coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the third coefficient: "))
if (a!=0.0):
    d = (b*b)-(4*a*c) 
    if (d==0.0):
        print("The roots are real and equal.") 
        r = -b/(2*a)
        print("The roots are ", r,"and", r)
    elif(d>0.0):
        print("The roots are real and distinct.")
        r1 = (-b+(math.sqrt(d)))/(2*a) 
        r2 = (-b-(math.sqrt(d)))/(2*a)
        print("The root1 is: ", r1)
        print("The root2 is: ", r2)
    else:
        print("The roots are imaginary.")
        rp = -b/(2*a)
        ip = math.sqrt(-d)/(2*a)
        print("The root1 is: ", rp, "+ i",ip)
        print("The root2 is: ", rp, "- i",ip)
else:
    print("Not a quadratic equation.")
Output:

Ezoic
Enter the first coefficient: 4
Enter the second coefficient: 7
Enter the third coefficient: 2
The roots are real and distinct.
The root1 is:  -0.3596117967977924
The root2 is:  -1.3903882032022077

18. Python program to print the numbers from a given number n till 0 using recursion

def print_till_zero(n):
    if (n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
print_till_zero(8)
Output:

Ezoic
8
7
6
5
4
3
2
1

19. Python program to find the factorial of a number using recursion

def fact(n):
    if n==1:
        f=1
    else:
        f = n * fact(n-1)
    return f
num = int(input("Enter an integer: "))
result = fact(num)
print("The factorial of", num, " is: ", result)
Output:

Enter an integer: 5
The factorial of 5  is:  120

20. Python program to display the sum of n numbers using a list

numbers = []
num = int(input('How many numbers: '))
for n in range(num):
    x = int(input('Enter number '))
    numbers.append(x)
print("Sum of numbers in the given list is :", sum(numbers))
Output:

How many numbers: 3
Enter number 2
Enter number 3
Enter number 4
Sum of numbers in the given list is : 9

21. Python program to implement linear search

numbers = [4,2,7,1,8,3,6]
f = 0 #flag
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
    if (x==numbers[i]):
        print("Successful search, the element is found at position", i)
        f = 1
        break
if(f==0):
    print("Oops! Search unsuccessful")
Output:

Enter the number to be found out: 7
Successful search, the element is found at position 2

22. Python program to implement binary search

def binarySearch(numbers, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if (numbers[mid] == x):
            return mid
        elif (numbers[mid] > x):
            return binarySearch(numbers, low, mid-1, x)
        else:
            return binarySearch(numbers, mid+1, high, x)
    else:
        return -1
numbers = [ 1,4,6,7,12,17,25 ]   #binary search requires sorted numbers
x = 7
result = binarySearch(numbers, 0, len(numbers)-1, x)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")
Output:

Ezoic
Search successful, element found at position  3

23. Python program to find the odd numbers in an array

numbers = [8,3,1,6,2,4,5,9]
count = 0
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        count = count+1
print("The number of odd numbers in the list are: ", count)
Ezoic
Output:

The number of odd numbers in the list are:  4

24. Python program to find the largest number in a list without using built-in functions

numbers = [3,8,1,7,2,9,5,4]
big = numbers[0]
position = 0
for i in range(len(numbers)):
    if (numbers[i]>big):
        big = numbers[i]
        position = i
print("The largest element is ",big," which is found at position ",position)
Output:

Ezoic
The largest element is  9  which is found at position  5

25. Python program to insert a number to any position in a list

numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the number to be inserted: "))
y = int(input("Enter the position: "))
numbers.insert(y,x)
print(numbers)
Output:

[3, 4, 1, 9, 6, 2, 8]
Enter the number to be inserted: 11
Enter the position: 2
[3, 4, 11, 1, 9, 6, 2, 8]

26. Python program to delete an element from a list by index

numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the position of the element to be deleted: "))
numbers.pop(x)
print(numbers)
Ezoic
Output:

Ezoic
[3, 4, 1, 9, 6, 2, 8]
Enter the position of the element to be deleted: 4
[3, 4, 1, 9, 2, 8]

27. Python program to check whether a string is palindrome or not

def rev(inputString):
    return inputString[::-1]
def isPalindrome(inputString):
    reverseString = rev(inputString)
    if (inputString == reverseString):
        return True
    return False
s = input("Enter a string: ")
result = isPalindrome(s)
if result == 1:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
Output:

Enter a string: malayalam
The string is palindrome
Enter a string: car
The string is not palindrome

28. Python program to implement matrix addition

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for k in result:
    print(k)
Output:

Ezoic
[16, 10, 4]
[18, 8, 9]
[13, 10, 4]

29. Python program to implement matrix multiplication

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for x in result:
    print(x)
Output:
Ezoic

Ezoic
[118, 69, 60, 0]
[117, 68, 50, 0]
[113, 62, 57, 0]

30. Python program to check leap year

year = int(input("Enter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, " is not a leap year")
Output:

Enter a year: 2023
2023 is not a leap year
Enter a year: 2024
2024 is a leap year

31. Python program to find the Nth term in a Fibonacci series using recursion

def Fib(n):
    if n<0:
        print("The input is incorrect.")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(7))
Output:

Ezoic
8

32. Python program to print Fibonacci series using iteration

a = 0
b = 1
n=int(input("Enter the number of terms in the sequence: "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a,b = b,c
    print(c,end=" ")
    n=n-1
Output:

Enter the number of terms in the sequence: 8
0 1 1 2 3 5 8 13

33. Python program to print all the items in a dictionary
phone_book = {
'John' : [ '8592970000', 'john@xyzmail.com' ],
'Bob': [ '7994880000', 'bob@xyzmail.com' ],
'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
}
for k,v in phone_book.items():
    print(k, ":", v)
Output:

Ezoic
John : ['8592970000', 'john@xyzmail.com']
Bob : ['7994880000', 'bob@xyzmail.com']
Tom : ['9749552647', 'tom@xyzmail.com']

34. Python program to implement a calculator to do basic operations

def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
print("Enter two numbers")
n1=input()
n2=input()
print("Enter the operation +,-,*,/ ") 
op=input() 
if op=='+':
    add(int(n1),int(n2))
elif op=='-':
    subtract(int(n1),int(n2))
elif op=='*':
    multiply(int(n1),int(n2))
elif op=='/':
    divide(int(n1),int(n2))
else:
    print(" Invalid entry ")
Output:

Ezoic
5
6
Enter the operation +,-,*,/ 
*
30

35. Python program to draw a circle of squares using Turtle
import turtle
x=turtle.Turtle()


def square(angle):
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle+10)

for i in range(36):
    square(90)
Output:1. Python program to check whether the given number is even or not.

number = input("Enter a number: ")
x = int(number)%2
if x == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
Output:

Enter a number: 7
The number is Odd.
Enter a number: 6
The number is Even.

2. Python program to convert the temperature in degree centigrade to Fahrenheit

c = input("Enter temperature in Centigrade: ")
f = (9*(int(c))/5)+32
print("Temperature in Fahrenheit is: ", f)
Output:

Enter temperature in Centigrade: 30
Temperature in Fahrenheit is:  86.0

3. Python program to find the area of a triangle whose sides are given

import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ", area)
Output:

Enter the length of side a: 4.0
Enter the length of side b: 3.0
Enter the length of side c: 6.0
Area of the triangle is:  5.332682251925386

4. Python program to find out the average of a set of integers

count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print("The average is: ", avg)
Output:

Enter the count of numbers: 5
Enter an integer: 3
Enter an integer: 6
Enter an integer: 8
Enter an integer: 5
Enter an integer: 7
The average is:  5.8

5. Python program to find the product of a set of real numbers

i = 0
product = 1
count = int(input("Enter the number of real numbers: "))
for i in range(count):
    x = float(input("Enter a real number: "))
    product = product * x
print("The product of the numbers is: ", product)
Ezoic
Output:

Enter the number of real numbers: 4
Enter a real number: 3.2
Enter a real number: 2.9
Enter a real number: 7.4
Enter a real number: 5.5
The product of the numbers is:  377.69599999999997

6. Python program to find the circumference and area of a circle with a given radius

import math
r = float(input("Input the radius of the circle: "))
c = 2 * math.pi * r
area = math.pi * r * r
print("The circumference of the circle is: ", c)
print("The area of the circle is: ", area)
Output:

Input the radius of the circle: 4.3
The circumference of the circle is:  27.01769682087222
The area of the circle is:  58.088048164875275

7. Python program to check whether the given integer is a multiple of 5

number = int(input("Enter an integer: "))
if(number%5==0):
    print(number, "is a multile of 5")
else:
    print(number, "is not a multiple of 5")
Output:

Enter an integer: 23
23 is not a multiple of 5
Enter an integer: 55
55 is a multile of 5

8. Python program to check whether the given integer is a multiple of both 5 and 7

number = int(input("Enter an integer: "))
if((number%5==0)and(number%7==0)):
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of both 5 and 7")

Ezoic
Output:

Enter an integer: 33
33 is not a multiple of both 5 and 7
Enter an integer: 35
35 is a multiple of both 5 and 7

9. Python program to find the average of 10 numbers using while loop

count = 0
sum = 0.0
while(count<10):
    number = float(input("Enter a real number: "))
    count=count+1
    sum = sum+number
avg = sum/10
print("Average is :",avg)
Output:

Enter a real number: 2.3
Enter a real number: 3.3
Enter a real number: 1.7
Enter a real number: 4.1
Enter a real number: 1.65
Enter a real number: 7.32
Enter a real number: 6.66
Enter a real number: 4.53
Enter a real number: 9.01
Enter a real number: 2.15 
Average is : 4.272

10. Python program to display the given integer in a reverse manner

number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    rev = (rev*10)+digit
    number = number//10
print(rev)
Output:

Enter a positive integer: 739
937

11. Python program to find the geometric mean of n numbers
c = 0
p = 1.0
count = int(input("Enter the number of values: "))
while(c<count):
    x = float(input("Enter a real number: "))
    c = c+1
    p = p * x
gm = pow(p,1.0/count)
print("The geometric mean is: ",gm)
Output:

Enter the number of values: 6
Enter a real number: 3.2
Enter a real number: 1.54
Enter a real number: 4.11
Enter a real number: 9.12
Enter a real number: 7.56
Enter a real number: 3.14
The geometric mean is:  4.045694954202098

12. Python program to find the sum of the digits of an integer using a while loop

sum = 0
number = int(input("Enter an integer: "))
while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digits is: ", sum)
Output:

Enter an integer: 395
Sum of digits is:  17

13. Python program to display all the multiples of 3 within the range 10 to 50

for i in range(10,50):
    if (i%3==0):
        print(i)
Output:
Ezoic

12
15
18
21
24
27
30
33
36
39
42
45
48

14. Python program to display all integers within the range 100-200 whose sum of digits is an even number

for i in range(100,200):
    num = i
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    if(sum%2==0):
        print(i)
Output:

101
103
105
107
109
110
112
114
116
118
121
123
125
127
129
130
132
134
136
138
141
143
145
147
149
150
152
154
156
158
161
163
165
167
169
170
172
174
176
178
181
183
185
187
189
190
192
194
196
198

15. Python program to check whether the given integer is a prime number or not

num = int(input("Enter an integer greater than 1: "))
isprime = 1 #assuming that num is prime
for i in range(2,num//2):
    if (num%i==0):
        isprime = 0
        break
if(isprime==1):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
Output:

Enter an integer greater than 1: 7
7 is a prime number
Enter an integer greater than 1: 24
24 is not a prime number

16. Python program to generate the prime numbers from 1 to N

num =int(input("Enter the range: "))
for n in range(2,num):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)   
Output:

Enter the range: 6
2
3
5

17. Python program to find the roots of a quadratic equation

import math
a = float(input("Enter the first coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the third coefficient: "))
if (a!=0.0):
    d = (b*b)-(4*a*c) 
    if (d==0.0):
        print("The roots are real and equal.") 
        r = -b/(2*a)
        print("The roots are ", r,"and", r)
    elif(d>0.0):
        print("The roots are real and distinct.")
        r1 = (-b+(math.sqrt(d)))/(2*a) 
        r2 = (-b-(math.sqrt(d)))/(2*a)
        print("The root1 is: ", r1)
        print("The root2 is: ", r2)
    else:
        print("The roots are imaginary.")
        rp = -b/(2*a)
        ip = math.sqrt(-d)/(2*a)
        print("The root1 is: ", rp, "+ i",ip)
        print("The root2 is: ", rp, "- i",ip)
else:
    print("Not a quadratic equation.")
Output:

Ezoic
Enter the first coefficient: 4
Enter the second coefficient: 7
Enter the third coefficient: 2
The roots are real and distinct.
The root1 is:  -0.3596117967977924
The root2 is:  -1.3903882032022077

18. Python program to print the numbers from a given number n till 0 using recursion

def print_till_zero(n):
    if (n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
print_till_zero(8)
Output:

Ezoic
8
7
6
5
4
3
2
1

19. Python program to find the factorial of a number using recursion

def fact(n):
    if n==1:
        f=1
    else:
        f = n * fact(n-1)
    return f
num = int(input("Enter an integer: "))
result = fact(num)
print("The factorial of", num, " is: ", result)
Output:

Enter an integer: 5
The factorial of 5  is:  120

20. Python program to display the sum of n numbers using a list

numbers = []
num = int(input('How many numbers: '))
for n in range(num):
    x = int(input('Enter number '))
    numbers.append(x)
print("Sum of numbers in the given list is :", sum(numbers))
Output:

How many numbers: 3
Enter number 2
Enter number 3
Enter number 4
Sum of numbers in the given list is : 9

21. Python program to implement linear search

numbers = [4,2,7,1,8,3,6]
f = 0 #flag
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
    if (x==numbers[i]):
        print("Successful search, the element is found at position", i)
        f = 1
        break
if(f==0):
    print("Oops! Search unsuccessful")
Output:

Enter the number to be found out: 7
Successful search, the element is found at position 2

22. Python program to implement binary search

def binarySearch(numbers, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if (numbers[mid] == x):
            return mid
        elif (numbers[mid] > x):
            return binarySearch(numbers, low, mid-1, x)
        else:
            return binarySearch(numbers, mid+1, high, x)
    else:
        return -1
numbers = [ 1,4,6,7,12,17,25 ]   #binary search requires sorted numbers
x = 7
result = binarySearch(numbers, 0, len(numbers)-1, x)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")
Output:

Ezoic
Search successful, element found at position  3

23. Python program to find the odd numbers in an array

numbers = [8,3,1,6,2,4,5,9]
count = 0
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        count = count+1
print("The number of odd numbers in the list are: ", count)
Ezoic
Output:

The number of odd numbers in the list are:  4

24. Python program to find the largest number in a list without using built-in functions

numbers = [3,8,1,7,2,9,5,4]
big = numbers[0]
position = 0
for i in range(len(numbers)):
    if (numbers[i]>big):
        big = numbers[i]
        position = i
print("The largest element is ",big," which is found at position ",position)
Output:

Ezoic
The largest element is  9  which is found at position  5

25. Python program to insert a number to any position in a list

numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the number to be inserted: "))
y = int(input("Enter the position: "))
numbers.insert(y,x)
print(numbers)
Output:

[3, 4, 1, 9, 6, 2, 8]
Enter the number to be inserted: 11
Enter the position: 2
[3, 4, 11, 1, 9, 6, 2, 8]

26. Python program to delete an element from a list by index

numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the position of the element to be deleted: "))
numbers.pop(x)
print(numbers)
Ezoic
Output:

Ezoic
[3, 4, 1, 9, 6, 2, 8]
Enter the position of the element to be deleted: 4
[3, 4, 1, 9, 2, 8]

27. Python program to check whether a string is palindrome or not

def rev(inputString):
    return inputString[::-1]
def isPalindrome(inputString):
    reverseString = rev(inputString)
    if (inputString == reverseString):
        return True
    return False
s = input("Enter a string: ")
result = isPalindrome(s)
if result == 1:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
Output:

Enter a string: malayalam
The string is palindrome
Enter a string: car
The string is not palindrome

28. Python program to implement matrix addition

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for k in result:
    print(k)
Output:

Ezoic
[16, 10, 4]
[18, 8, 9]
[13, 10, 4]

29. Python program to implement matrix multiplication

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for x in result:
    print(x)
Output:
Ezoic

Ezoic
[118, 69, 60, 0]
[117, 68, 50, 0]
[113, 62, 57, 0]

30. Python program to check leap year

year = int(input("Enter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, " is not a leap year")
Output:

Enter a year: 2023
2023 is not a leap year
Enter a year: 2024
2024 is a leap year

31. Python program to find the Nth term in a Fibonacci series using recursion

def Fib(n):
    if n<0:
        print("The input is incorrect.")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(7))
Output:

Ezoic
8

32. Python program to print Fibonacci series using iteration

a = 0
b = 1
n=int(input("Enter the number of terms in the sequence: "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a,b = b,c
    print(c,end=" ")
    n=n-1
Output:

Enter the number of terms in the sequence: 8
0 1 1 2 3 5 8 13

33. Python program to print all the items in a dictionary
phone_book = {
'John' : [ '8592970000', 'john@xyzmail.com' ],
'Bob': [ '7994880000', 'bob@xyzmail.com' ],
'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
}
for k,v in phone_book.items():
    print(k, ":", v)
Output:

Ezoic
John : ['8592970000', 'john@xyzmail.com']
Bob : ['7994880000', 'bob@xyzmail.com']
Tom : ['9749552647', 'tom@xyzmail.com']

34. Python program to implement a calculator to do basic operations

def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)
print("Enter two numbers")
n1=input()
n2=input()
print("Enter the operation +,-,*,/ ") 
op=input() 
if op=='+':
    add(int(n1),int(n2))
elif op=='-':
    subtract(int(n1),int(n2))
elif op=='*':
    multiply(int(n1),int(n2))
elif op=='/':
    divide(int(n1),int(n2))
else:
    print(" Invalid entry ")
Output:

Ezoic
5
6
Enter the operation +,-,*,/ 
*
30

35. Python program to draw a circle of squares using Turtle
import turtle
x=turtle.Turtle()


def square(angle):
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle+10)

for i in range(36):
    square(90)
Output:




    iii^
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
^
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~

