import sys

"""
1 . Write a program in Python to perform the following operation: 
If a number is divisible by 3 it should print Consultadd as a string
If a number is divisible by 5 it should print Python Training as a string
If a number is divisible by both 3 and 5 it should print Consultadd - Python Training as astring. 

"""


"""
print("Enter a number:")
x = int(input())

if x % 3 == 0 and x % 5 != 0: 
    print("Consultadd\n")

elif x % 3 != 0 and x % 5 == 0: 
    print("Python Training\n")

elif x % 3 == 0 and x % 5 == 0: 
    print("Consultadd - Python Training\n")
else:
    print("Number is not multiple of 3 or 5 \n")  """

# 2.Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2 and
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average assoon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying NEGATIVE
# At a time a user can only perform one action.1. Write a program in Python to perform the following operation:

"""
print ("Choose the following options:\n Enter 1 - Addition\n Enter 2 - Subtraction\n " + 
            "Enter 3 - Division\n Enter 4 - Multiplication\n Enter 5 - Average ")

x = int(input())

if x > 0 and x <= 5:
    print("Enter two numbers:\n")
    num1 = float(input())
   
    num2 = float(input())
  
    if x == 1:
        res = num1 + num2
    elif x == 2:
        res = num1 - num2
    elif x == 3:
        res = num1 / num2
    elif x == 4:
        res = num1 * num2
    else: 
        print("Enter two more numbers:\n")
        first  = float(input())
      
        second = float(input())
       
        res = (num1+num2+first+second)/4
    if (res<0):
        print("Negative result\n")
    else:
        print("\n result =", res)

else:
    print("Enter valid choice:")

"""
"""
print("Enter three numbers of average:")
a = int(input())
b = int(input())
c = int(input())

avg = (a+b+c)/3

if (avg > a and avg > b and avg > c):
    print("\nAverage is higher than a,b,c \n")
elif (avg > a and avg > b and avg < c):
    print("\nAverage is higher than a,b \n")
elif (avg > b and avg > c and avg < a):
    print("\nAverage is higher than b,c \n")
elif(avg > a and avg > c and avg < b):
    print("\nAverage is higher than a,c \n")
elif(avg > a and avg < c and avg < b):
    print("\nAverage is higher than a only \n")
elif(avg < a and avg >b and avg < c):
    print("\nAverage is higher than b only \n")
elif(avg < a and avg < b and avg > c):
    print("\nAverage is higher than c only \n")
    """


#  Write a program in Python to break and continue if the following cases occurs:
#  If user enters a negative number just break the loop and print Its Over
#  If user enters a positive number just continue in the loop and print Good Going  

"""
print("Input a number:")
x =int(input())
while (x):
    if (x<0):
        break
    else:
        print("It's going good")
        print("Input a number:")
        x =int(input())
"""

#5.Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

"""
for i in range(2000,3200):
    if (i%7==0 and not(i % 5 == 0)):
        print(i)
        """
#6. What is the output of the following code examples?
"""
x =123        
for i in x:
    print(i)
"""
# output : TypeError: 'int' object is not iterable
"""
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
"""
""" output

0
error
1
error
2
"""

"""
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break
"""
# output: NameError: name 'Break' is not defined

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.Expected output: 0 1 2 4 5 Note: Use continue statement
"""
x = 0
while (x<=6):
    if ((x == 3) or (x == 6)):
        x += 1
        continue
    else:
        print(x)
    x += 1 """
# 8. Write a program that accepts a string as an input from the user and calculate the number of digitsand letters.
# Sample input: consul72 Expected output: Letters 6 Digits 2

"""
userInput = input("Enter your input : ")
letters = 0
digits = 0
for x in userInput:
    if x.isalpha():
        letters += 1
    elif x.isdigit():
        digits += 1
    else:
        print("Invalid input")

print("Letters", letters, "Digits", digits)
"""
  
"""
luckyNumber = 4

while True:
    userGuess = int(input("Guess the lucky number : "))

    if userGuess == luckyNumber:
        print(f'Bingo. Your guess is correct.')
        break
    else:
        print(f'Better luck next time.')

    answer = input("Do you want to guess again, say Yes or No: ")

    if answer == "No":
        break
    elif answer == "Yes":
        continue

"""


