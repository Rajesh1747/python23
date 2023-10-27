#Certainly! Here are 20 more Python programs that use for loops for various tasks:

#11. *Count the Number of Vowels in a String:*
#python
text = "Hello, World"
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count += 1
print(f"Number of vowels: {count}")


#12. *Calculate the Sum of Even Numbers from 1 to N:*
#python
N = 10
sum = 0
for i in range(2, N + 1, 2):
    sum += i
print(f"Sum of even numbers from 1 to {N}: {sum}")


#13. *Print the ASCII Values of Characters:*
#python
text = "Hello"
for char in text:
    print(f"ASCII value of {char} is {ord(char)}")


#14. *Generate a Simple Calendar:*
#python
import calendar

year = 2023
month = 4
cal = calendar.month(year, month)
print(cal)


#15. *Calculate the Average of Numbers in a List:*
#python
numbers = [5, 10, 15, 20, 25]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(f"Average: {average}")


#16. *Find the Largest Number in a List:*
#python
numbers = [15, 8, 21, 36, 42, 7]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Largest number: {max_num}")


#17. *Calculate the GCD (Greatest Common Divisor) of Two Numbers:*
#python
import math

a = 36
b = 48
gcd = math.gcd(a, b)
print(f"GCD of {a} and {b}: {gcd}")


#18. *Check for Prime Numbers:*
#python
N = 17
is_prime = True
for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        is_prime = False
        break
print(f"{N} is prime: {is_prime}")


#19. *Calculate the Power of a Number:*
#python
base = 2
exponent = 3
result = 1
for _ in range(exponent):
    result *= base
print(f"{base}^3 = {result}")


#20. *Print the First N Terms of the Harmonic Series:*
#python
N = 5
harmonic_sum = 0
for i in range(1, N + 1):
    harmonic_sum += 1 / i
print(f"Sum of first {N} terms of the Harmonic Series: {harmonic_sum}")


#21. *Calculate the Mean of Multiple Lists:*
#python
list1 = [10, 20, 30, 40, 50]
list2 = [5, 15, 25, 35, 45]
mean_list = []
for i in range(len(list1)):
    mean_list.append((list1[i] + list2[i]) / 2)
print(f"Mean of corresponding elements: {mean_list}")


#22. *Print the Characters of a String in Reverse Order:*
#python
text = "Python"
reverse_text = ""
for char in reversed(text):
    reverse_text += char
print(f"Reversed string: {reverse_text}")


#23. *Find the Median of a List of Numbers:*
#python
numbers = [7, 3, 2, 8, 4]
numbers.sort()
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n // 2] + numbers[n // 2 - 1]) / 2
else:
    median = numbers[n // 2]
print(f"Median: {median}")


#24. *Print a Diamond Pattern:*
#python
N = 5
for i in range(N):
    print(" " * (N - i - 1) + "*" * (2 * i + 1))
for i in range(N - 2, -1, -1):
    print(" " * (N - i - 1) + "*" * (2 * i + 1))


#25. *Check for Palindromic Words in a Sentence:*
#python
sentence = "A man a plan a canal Panama"
words = sentence.split()
palindromes = [word for word in words if word.lower() == word.lower()[::-1]]
print(f"Palindromic words: {palindromes}")


#These are additional Python programs that use for loops for various tasks. You can run them in a Python environment to see how they work.
