#                                         ASSIGNMENTS
# TASKONE: NUMBERS AND VARIABLES
# 1.Create three variables in a single line and assign different values to them and make sure their data types are different.\
# Like one is int, another one is float and last one is string.
"""
x, y, z = 3, 5.6, "Python"
# 2. 	Create a variable of value type complex and swap it with another variable whose value is an integer.

x = 4 + 2j
y = 7
print("Values of x and y before swapping: ", x, y)
# swapping X and Y
x, y = y, x
print("Values of x and y after swapping: ", x, y)

# 3. 	Swap two numbers using third variable as result name and do the same task without using any third variable.

x, y = 5, 6
print("Values of x and y before swapping: ", x, y)
# swapping using 3rd variable "z"
z = x
x = y
y = z
print("Values of x and y after swapping(using 3rd variable: ", x, y)
# swapping without using 3rd variable "z"
x, y = y, x
print("Values of x and y after second swap (without using 3rd variable): ", x, y)

# 4.Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.

# Using python 2.x
# using raw_input()
x = raw_input("enter any value: ")
print("value of x is: ", x)
# Using input()
x = input("enter any value: ")
print("value of x is: ", x)

# Using python3.x
x = input("enter any value: ")
print("value of x is: ", x)
# 5. 	Write a program to complete the task given below:
# Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable  call z.
# Use z for adding 30 into it and print the final result by using variable result.

x, y = eval(input("input any two numbers between 1 to 10: "))
z = x + y
# Use z for adding 30 into it and print the final result by using variable result.
result = z + 30
print("Final Result is:", result)

# 6. 	Write a program to check the data type of the entered values.
# HINT: Printed output should say -  The input value data type is : int/float/string/etc
x = eval(input("enter any value: "))
print(" The input value datatype is: ", type(x))
# 7.Create Variable using
# CamelCase, LadderCase and UPPERCASE.(Refer: https: // capitalizemytitle.com / camel - case /)
# Solution:
FirstVar = 10  # UpperCamelCase
firstVar = 101  # lowerCamelCase
first_var = 20  # snake_case/ladder_case
FIRSTVAR = 30  # UPPERCASE
#
# 8. 	If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again.
# Will it change the value. If Yes then Why?
Yes! The value of a will be changed to whichever value is assigned last irrespective of data type.
Because the value at the memory location of the variable ‘a’ is being changed/overridden.

# TASK TWO: OPERATORS AND DECISION MAKING STATEMENT
# 1.	Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “c” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.

x = int(input("enter any number: "))
if x % 3 == 0 and x % 5 != 0:
    print("Consultadd")
if x % 5 == 0 and x % 3 != 0:
    print("c")
if x % 3 == 0 and x % 5 == 0:
    print("Consultadd Python Training")

# 2. 	Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If USer Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
# Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option 5.
# At the end if the answer of any operation is Negative print a statement saying “zsa”
# NOTE: At a time user can perform one action at a time.

x = int(input(" Enter 1 - Addition \n Enter 2 - Subtraction \n Enter 3 - Division \n "
              "Enter 4 - Multiplication \n Enter 5 - Average \n"
              " Enter any number from the above options: "))
output = 0
if x in range(6):
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    if x == 1:
        output = first + second
    elif x == 2:
        output = first - second
    elif x == 3:
        output = first / second
    elif x == 4:
        output = first * second
    elif x == 5:
        print("Please enter two more numbers to calculate average")
        first1 = int(input("Enter first1 number: "))
        second2 = int(input("Enter second2 number: "))
        output = (first + first1 + second + second2) / 4
    if output < 0:
        print("zsa")
    else:
        print("The output is:", output)
else:
    print(" Invalid Entry")

# 3. 	Write a program in Python to implement the given flowchart:
a = 10
b = 20
c = 30
avg = (a + b + c) / 3
print("avg = ", avg)

if avg > a and avg > b and avg > c:
    print("Average is greater than a, b,c")
else:
    if avg > a and avg > b:
        print("avg is higher than a, b, c")
    elif avg > a and avg > c:
        print("avg is higher than a , c")
    elif avg > b and avg > c:
        print("avg is higher than b, c")
    elif avg > a:
        print("avg is just higher than a")
    elif avg > b:
        print("avg is just higher than b")
    elif avg > c:
        print("avg is just higher than c")

# 4. 	Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”

while True:
   x = int(input("Enter any number: "))
   if x<0:
       print("It's Over")
       break
   else:
       print("Good Going")
       Continue
#
# 5.   Write a program in Python which will find all such numbers which are divisible  by 7 but are not a multiple of 5,
# between 2000 and 3200.

for i in range(2000, 3201):
   if i % 7 == 0:
       if i % 5 != 0:
           print(i)
       else:
           Continue

# 6. What is the output of the following code examples?
#    x=123
#    	   for i in x:
#    		print(i)

# Output:
# TypeError: 'int' object is not iterable
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(“error”)
# Output:
# 0 1 2
#
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break
# Output:
# 0 1 2 3 4

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#        Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

i = 0
for i in range(7):
   if i == 3 or i == 6:
       continue
   else:
       print(i)
#
# 8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

x = input("enter an alphanumeric string: ")
a = b = 0
for i in x:
   if i.isalpha():
       a += 1
   elif i.isdigit():
       b += 1
print("Letters: ", a)
print("Digits: ", b)


# 9. Read the two parts of the question below:
#  Write a program such that it asks users to “guess the lucky number”.
#  If the correct number is guessed the program stops, otherwise it continues forever.

x = randrange(10)
while True:
   y = int(input("Guess the lucky number between 1 to 10: "))
   if x == y:
       print("Your guess is correct !! Lucky number is: ", x)
       break
   else:
       continue

# Modify the program so that it asks users whether they want to guess again each time.
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing.
# The program stops if the user guesses the correct number or answers “no”.
# ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

x = randrange(10)
while True:
   number = int(input("Guess the lucky number between 1 to 10: "))
   if x == number:
       print("Your guess is correct !! Lucky number is: ", x)
       break
   else:
       answer = input("Incorrect Guess!! Do you want to continue guessing? (yes/no): ")
       if answer.lower() == "yes":
           continue
       elif answer.lower() == "no":
           break
       else:
           print("Invalid entry")

# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
#            		counter=1
# 		While counter <= 5:
# 			print(“Type in the”, counter, “number”
# 			counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not).
# If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.

number = randrange(10)
count = 1
#print("Guessed number is: ", number)
while count <= 5:
   print("Type in the", count, "number")
   guessedNumber = int(input())
   count += 1

   if number == guessedNumber:
       print("Good Guess!")
   else:
       print("Try again!")
   if count > 5:
       print("Game Over!")

# 11. In the previous question, insert “break” after the “Good guess!”
# print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number.
# If the user does not guess the number at all, print “Sorry but that was not very successful”.

number = randrange(10)
count = 1
#print("Guessed number is: ", number)
while count <= 5:
   print("Type in the", count, "number")
   guessedNumber = int(input())
   count += 1

   if number == guessedNumber:
       print("Good Guess!")
       break
   elif count <= 5:
       print("Try again!")
   else:
       print("Sorry but that was not very successful")
print("Game Over!")

#
# TASK THREE: DATA STRUCTURES
# 1.	Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.

a = [1,2,3.4,5.6,1+2j,8+3j,"Python","Training","list",7]

# 2. 	Create a list of size 5 and execute the slicing structure
a = [1,2,3.4,5.6,1+2j]
print(a[:]) # Prints entire list
print(a[1:4])
print(a[::-1])
print(a[::2])

# 3. Write a program to get the sum and multiply of all the items in a given list.

a = [1,2,3,4,5]
sum=0
mul= 1
for i in a:
   sum += i
   mul *= i
print("sum of all numbers in list: ", sum)
print("Multiplication total of numbers in list: ", mul)

# 4.  Find the largest and smallest number from a given list.

a = [1,2,3,4,5]
print("largest number in list is: ", max(a))
print("smallest number in list is: ", min(a))

# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

lst = [2,3,5,6,8,11,7]
elst = []
for i in lst:
   if i%2 != 0 :
       elst.append(i)
print("New list is: ", elst)

# 6.	Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

lst = []
for i in range(1, 31):
   lst.append(i**2)
print("List of first five elements: ", lst[:5])
print("List of last five elements: ", lst[-5:])

#
# 7.	Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

l = [1,3,5,7,9,10]
l1 = [2,4,6,8]

l[-1:] = l1
print(l)
#
# 8.	Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

# 9.Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

n = int(input("enter any number: "))
d = {}
for i in range (1,n+1):
   d[i] = i**2
print(d)
#
# 10. 	Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

n = input("enter some numbers seperated by commas: ")
lst = n.split(",")
tup = tuple(lst)
print("list is: ", lst)
print("tuple is: ", tup)


MORE QUESTIONS ON DATA STRUCTURES

#
# 1.	Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
# Same as first question in task 3
#
# 2. 	Create a list of size 5 and execute the slicing structure
# Same as second question in task 3
# 3. 	Create a list of given structure and run

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list [1, 2, 3, 4]
print(x[5][:4])
# Access list [600,  700]
print (x[-3:-1])
# Access list [100, 300, 500, 600, 800]
print(x[::2])
# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])
# Access list [10]
print(x[10]): Index Error
# Access list [ ]
print(x[:])

# 5. 	How Tuple is beneficial as compare to the list?
# Tuple is immutable while list is mutable.  Therefore they are faster. Can be used as dictionary keys.

# 6. 	Write a program in Python to iterate through the list of numbers in the range of 1,100 and
# print the number which is divisible by 3 and a multiple of 2.

for i in range(1100):
   if i%3 == 0 and i%2 == 0:
       print(i)

# 7. 	Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.

s = input("enter any string: ")
s1 = ""
count=0
for i in s:
   s1 = i+s1
print(s1)
for x in s1:
   if x in 'AaEeIiOoUu':
       print(count,x)
   count += 1

# 8. Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.

s = "hello my name is abcde"
for i in range(len(s)):
   if i%2==0:
       print(s[i])

# 9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]

x=[1,2,3,4,5,6,7,8,9,-1]
for i in x:
   for j in x:
       if i != j:
           if x[i] + x[j] == 8 :
               print(x[i],x[j])

# 10. 	Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
# Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

Solution:
even_list = list()
odd_list = list()
even_sum = 0
odd_sum = 0
while True:
   if len(even_list) == 5 and len(odd_list) == 5:
       break
   else:
       x = int(input("enter any number between 1 to 50: "))
       if x % 2 == 0:
           if len(even_list) < 5:
               even_list.append(x)
               even_sum += x
           else:
               print("you reached maximum elements even list")

       else:
           if len(odd_list) < 5:
               odd_list.append(x)
               odd_sum += x
           else:
               print("you reached maximum elements in odd list")

print("even list is: ", even_list, "sum of even list is: ", even_sum)
print("odd list is: ", odd_list,"sum of odd list is: ", odd_sum)
print("Max of list is ", max(even_sum,odd_sum))


# 11. Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab
#                       Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

alpha = 0
num = 0
x = input("enter any alphanumeric word: ")
y = set(x)
for i in y:
   if i.isalpha():
       print(i,x.count(i))

# 12.Generate and print another tuple whose values are even numbers in the giv
# en tuple (1,2,3,4,5,6,7,8,9,10).

t = (1,2,3,4,5,6,7,8,9,10)
lst = []
for i in t:
   if i%2 == 0:
       lst.append(i)
print(tuple(lst))
#
# TASK FOUR: FUNCTIONS
# 1. 	Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

def rev(s):
   n_string = ""
   length = len(s)
   while length > 0:
       n_string += s[length -1]
       length-= 1
   return n_string

print(rev("testing"))

# 2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def letter_case():
   x = input("enter any string: ")
   ucount = 0
   lcount = 0
   for i in x:
       if i.isupper():
           ucount += 1
       elif i.islower():
           lcount += 1
   print("No. of Uppercase characters: ", ucount)
   print("No. of Lowercase characters: ", lcount)

letter_case()

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def uList(l):
   lst = []
   for i in l:
       if i not in lst:
           lst.append(i)
   return lst

print(uList([1,2,3,4,5,5,7,7,6]))

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

x = list(input("enter hypen seperated list of words: ").split("-"))
x.sort()
print('-'.join(x))

# 5.Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

S =[]
while True:
   x = input()
   if x:
       s.append(x.upper())
   else:
       break
for i in s:
   print(i)

6.Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def add(str1, str2):
   a = int(str1)
   b = int(str2)
   print(a + b)


add("3", "4")

# 7. Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

def len_string(a,b):
   if len(a) > len (b):
       print(a)
   elif len(b) > len(a):
       print(b)
   else:
       print(a)
       print(b)

len_string("Python","traiin")

# 8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
def tup():
   t = tuple(map(lambda x:x**2, range(1,20)))
   return t

print(tup())

# 9. Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD


def showNumbers(limit):
   x = range(limit + 1)
   for i in x:
       if i % 2 == 0:
           print(i, "EVEN")
       else:
           print(i, "ODD")
showNumbers(5)


# 10.Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
y = filter(lambda x:x%2==0,range(1,21))
print(list(y))
#
# 11. 	Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	     Use filter() to filter elements of a list
#             Use lambda to define anonymous functions
x = [1,2,3,4,5,6,7,8,9,10]
y = map(lambda x: x**2,filter(lambda x:x%2==0,x))
print(list(y))
12. 	Write a function to compute 5/0 and use try/except to catch the exceptions
Solution:
def func():
   try:
       x = 5/0
   except:
       print("cannot divide by zero")
func()
#
# 13. 	Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567

from functools import reduce
l = [[1,2,3],[4,5],[6,7,8]]
l1 = reduce(lambda x,y: x+y, l)
print(l1)

#  14. 	What is the output of the following codes:
# (i) def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)
# Output:  2
#
# (ii) def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# a()
# Output:  “after f” is printed and faced the following error:
#  f(x, 4)
# NameError: name 'f' is not defined



TASK FIVE: FILE HANDLING AND EXCEPTION HANDLING
#
# 2. 	Write a program in Python to allow user to open a file by using argv module.
# If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.

while True:
   try:
       f = open(file_name,'r')
       data = f.read()
   except:
       print("Please check the name entered")
       file_name = input("enter the file name again: ")

   else:
       print("File read successfully")
       f.close()
       break

#
# 3. 	Write a program to handle an error if the user entered the number more than four digits it should return
# “Please length is too short/long !!! Please provide only four digits”

def dlen():
   x= input("enter any 4 digit number: ")
   while True:

       if x.isdigit():

           if len(x) > 4:
               print("Please length is too short/long !!! Please provide only four digits")
               x = (input("enter any 4 digit number: "))
           else:
               print("number entered:", x)
               break
       else:
           print("please enter a numeric value")
           x = (input("enter any 4 digit number: "))

# 4. 	Create a login page backend to ask user to enter the UserEmail and password.
# Make sure to ask Re-Type Password and if the password is incorrect give chance to
# enter it again but it should not be more than 3 times.

def login():
   email = input("Enter username: ")
   pwd = input("Enter Password: ")
   pwd1 = "Test123"
   count = 0
   while count < 3:
       if pwd == pwd1:
           print("login successful!! ")
           break
       else:
           if count == 2:
               print("Incorrect Password! Sorry!! Done with 3 attempts!! ")
               break
           else:

               print("Incorrect Password!! Please enter correct password!")
               pwd = input("Enter Password: ")
               count += 1


login()

#
# 6. 	Read any file using Python File handling concept and return only the even length string from the doc.txt file.
# Consider the content as:
# 	Hello I am a file
# 	Where you need to return the data string
# 	Which is of even length
# 	Make sure you return the content in
# 	The same link as it is present.

from sys import argv
program_name, file_name = argv
while True:
   try:
       f = open(file_name,'r')
       data = f.readlines()
       lines = list(data)[1::2]

   except:
       print("Please check the name entered")
       file_name = input("enter the file name again: ")
   else:
       print(lines)
       break
       f.close()

# TASK SIX: CLASSES AND OBJECTS
# 1.	Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math

C = 50
H = 30
D1 = [int(x) for x in input("enter numbers seperated by comma: ").split(",")]
Q = [ math.sqrt((2*C*D)/H) for D in D1 ]
print (Q)

# 2.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

class Shape:
   area = 0
   def area(self):
       len = 5
       area = len**2
       print("area of shape is", area)

class Square(Shape):
   def __init__(self,len):
       self.len = len
   def area(self):
       area = self.len**2
       print("area of square is", area)


s=Shape()
s.area()

s1 = Square(7)
s1.area()


# 3. Create a class to find the three elements that sum to zero from a set of n real numbers.
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Output: [[-10,2,8],[-7,-3,10]]

class three_ele:
   def ele(self,list):
       self.list = list
       for i in range(len(list)):
           for j in range(i+1, len(list)):
               for k in range(j+1, len(list)):
                   if list[i]+list[j]+list[k] == 0:
                       print([list[i],list[j],list[k]])

t = three_ele()
t.ele([-25,-10,-7,-3,2,4,8,10])

# 4.          What is the output of the following code? Explain your answer as well.
# a.Faced error as super class __init__was not called used Super() function in child class
# b.1,2
# c.Class B calls constructor of A and assigned value 3 to x, y is incremented by y when Class B method count is called.
# Hence output displays value of x and y as 3,1
# d.Class B is inheriting class A and calling class A constructor which inturn calls multiply function assigning value of i to 15.
# As the object called is of class B, class B multiply function is called and the value of i is multiplied by 2.
# Hence 30 is returned as output.

# 5.	Create a Time class and initialize it with hours and minutes.
# Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Make a method displayTime which should print the time.
# Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

class Time:
   def __init__(self, hours, minutes):
       self.hours = hours
       self.minutes = minutes

   def addTime(self,t1,t2):
       self.t1 = t1
       self.t2 = t2
       total = Time(0, 0)
       if t1.mins + t2.mins > 60:
           total.hours = (t1.mins + t2.mins) / 60
       total.hours = total.hours + t1.hours + t2.hours
       total.mins = (t1.mins + t2.mins) - ((((t1.mins + t2.mins) / 60) * 60))
       return total
   def displayTime(self):
       print("Time is: ", self.hours,self.minutes)

   def displayMinute(self):
       print( "Total Minutes",((self.hours *60) + self. minutes))

t1 = Time(2,50)
t2 = Time(1,20)
t1.displayTime()
t1.displayMinute()
total = Time.addTime(t1,t2)
total.displayTime()
# t3 = Time.addTime(t1,t2)
# t3.displayTime()
# t3.displayMinute()


"""