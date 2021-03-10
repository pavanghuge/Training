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


    
    






