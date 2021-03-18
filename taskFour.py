#1.Write a program to reverse a string.
# Sample input:“1234abcd”
# Expected output:“dcba4321”
input = "1234abcd"
length = len(input)
new_str =""
while (length >0):
    new_str += input[length-1]
    length -= 1
print(new_str)   

#2.Write a function that accepts a string and prints the number of uppercase letters 
# and lowercaseletters. Sample input:“abcSdefPghijQkl”Expected Output: No. of Uppercase 
# characters : 3 No. of Lower case Characters : 12

input = "abcSdefPghijQkl"

d = {"Lower":0,"Upper":0}

for i in input:
    if i.islower():
        d["Lower"] += 1
    elif i.isupper():
        d["Upper"] += 1
    else:
        pass

print("No. of Uppercase  characters :",d["Upper"],"No. of Lower case Characters :" ,d["Lower"])




# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

input = [1,2,3,4,5,2,1,2,3,4,3,2,1,2]

def unique(input):
    new_list = list(set(input))
    return new_list

newList = unique(input)
print(newList)


# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints 
# the words in a hyphen-separated sequence after sorting them alphabetically.

myInput = "My-name-is-Pavan"
sentence = myInput.split("-")
sentence.sort()
newSentence = " ".join(sentence)
print(newSentence)



# 5. Write a program that accepts a sequence of lines as input and prints the lines after 
# making allcharacters in the sentence capitalized.Sample input: Hello world Practice makes 
# man perfectExpected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

input = "Hello world Practice makes man perfect"
newInput = input.upper()
print(newInput)


#6. Define a function that can receive two integral numbers in string form and compute 
# their sum andprint it in the console.

def add(s1,s2):
    addition = 0
    addition = int(s1) +  int(s2)
    print(addition)

add("1","2")


#7. Define a function that can accept two strings as input and print the string with 
# the maximum length in the console. If two strings have the same length, then the function
#  should print both the strings lineby line.

def longerStr(s1,s2):
    if(len(s1)>len(s2)):
        print(s1)
    elif (len(s1)==len(s2)):
        print(s1 + " " + s2)
    else:
        print(s2)
longerStr("Pavan","Ghuge")
longerStr("Teju", "Pavan")
longerStr("Bhargav","Pavan")


# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).


def squares():
    return tuple([x**2 for x in range(1,21)])
print(squares())



# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.

def showNumbers(limit):
    for i in range(0,limit+1):
        if i % 2 == 0:
            print(i," Even ")
        else:
            print(i," Odd ")

showNumbers(3)


#10. Write a program which uses filter() to make a list whose elements are even numbers between 1 
# and 20 (both included)

x = filter(lambda x: x % 2 == 0, range(1,21)) 
print(list(x))

#11.Write a program which uses map() and filter() to make a list whose elements are squares of evennumbers
#  in [1,2,3,4,5,6,7,8,9,10].

x = map(lambda x: x ** 2,filter(lambda x: x % 2 == 0,range(1,11)) ) 
print(list(x))


# 12.Write a function to compute 5/0 and use try/except to catch the exceptions
def div(a,b):
    return a/b

def tryExcept():
    try:
        div(5,0)
    except ZeroDivisionError:
        print("Division by Zero Error")

tryExcept()
    

#13. Flatten the list[1,2,3,4,5,6,7] into 1234567 using reduce().
import functools
y = [1,2,3,4,5,6,7]
x = functools.reduce(lambda a,b : a*10 +b,y)
print(x)



# 14. Write a program in Python to find the values which are not divisible by 3 but 
# are a multiple of 7.Make sure to use only higher order functions.

x =[i for i in range (1,100) if i % 3 !=0 and i % 7 ==0]
print(x)

#15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

elements = [1,2,2,3,4,5,65,6,677]
def mul(i):
    return i*i

squares = map(mul,elements)
print(list(squares))


# 16. What is the output of the following codes:
def foo():
    try:
        return 1
    finally:
        return 2

k = foo()
print(k)



def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')

a()

# Ans :
# after f
# after f?
#    f(x, 4)
# NameError: name 'f' is not defined







