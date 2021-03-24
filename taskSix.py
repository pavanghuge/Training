

#1. Write a program in Python to find out the character in a string
#  which is uppercase using list comprehension.
x = [letter for letter in "PaVaN" if letter.isupper() ]
print(x)  


#2.Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System'] 
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System'] 
output = dict(zip(students,subjects))
print((output))

#4.Write a program in Python using generators to reverse the string.Input: String = “Consultadd Training”
string = "Consultadd Training"
def gen(string):
    s1 = " "
    for c in string:
        s1 = c + s1
        yield s1

reversedLetter = gen(string)
for i in range(len(string)):
    print(next(reversedLetter))


#5.Write an example on decorators.

def myDecorator(functionName):
    def innerFunc():
        print("Decorator Started:")
        functionName()
        print("Decorator ended")  
    return innerFunc()
 
@myDecorator 
def myfunction():
    print("This function is using decorator.")

