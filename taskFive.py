#1. Write a program in Python to allow the error of syntax to be handled using
# exception handling.HINT: Use SyntaxError

try:
    b = 10
    print(b)
    eval('a === 10')
except SyntaxError:
    print("Caught syntax error")
    print("You can only catch SyntaxError if it's thrown out of an eval, exec, or import operation.")


#2. Write a program in Python to allow the user to open a file by using the argv module. 
# If the entered name is incorrect throw an exception and 
# ask them to enter the name again. Make sureto use read only mode.
import sys  
try:
    filename = sys.argv[1]
    f = open('filename','r')
    print("File opened. Ready to write.")
    f.close()
except IndexError:
    print("Enter filename after program filename.")
except IOError:
    print("File not found")


#3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”

try :
    input = int(input("Enter a four digit number: "))
    if input < 1000 or input > 9999:
        raise ValueError
except ValueError:
    print("The length is too short/long !!! Please provide only four digits.")


#4.Create a login page backend to ask users to enter the username and password. 
# Make sure toask for a Re-Type Password and if the password is incorrect give 
# chance to enter it again but it should not be more than 3 times.



print("\nUser Authentication:")
userName = input("\nEnter username:")
pass_word = input("\nEnter password:") 

try:
    trials = 0
    while (userName != "pavan" and pass_word != "ghuge" ):
        print("\nUser Authentication:")
        userName = input("\nEnter username:")
        pass_word = input("\nEnter password:") 
        trials += 1
    
        if trials == 2:
            raise ValueError
            break

except ValueError:
    print("\nSorry you have exceeded 3 attempts to login.")
    print("\nLogin Unsuccessful!!! ")


    #6.Read doc.txt file using Python File handling concept and r
    # eturn only the even length string from the file. Consider the content of doc.txt as given below:
import sys
fileName = open("doc.txt","r")

for line in fileName.readlines():
    words = line.split(" ")
    for word in words:
        if len(word)%2 ==0:
            print(word)

fileName.close()

