
#1. Create a list of given structure and get the Access list as provided below
x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][0:5]) # Access list: [1, 2, 3, 4]
print(x[6:8]) # Access list: [600,700]
print(x[::-1]) # Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
y = []
y.append(x[5][5][0]) # Access list: [10]
print(y)
print([]) # Access list: [ ]

#2. Create a list of thousand numbers using range and xrange and see the difference between eachother.

#4.Write a program in Python to iterate through the list of numbers in the range of 1,100 and printthe number which is 
# divisible by 3 and is a multiple of 2.

for i in range(1,101):
    if(i%6 == 0):
        print(i) 

#5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists 
# in thestring with their index.

string = "love"
vowels = ["a","e","i","o","u"]
reverseString = string[::-1]
for x in reverseString:
    if x in vowels:
        print(x)

#6. 6.Write a program in Python to iterate through the string “hello my name is abcde” and 
# print thestring which is having an even length.
string = "hello my name is abcde"
sentence =string.split(" ")
for word in sentence:
    if (len(word) % 2 == 0):
        print(word)

#7.Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8. 
x = [1,2,3,4,5,6,7,8,9,-1]
result = 8
s = set()
for i in x:
    temp = result - i
    if (temp in s):
        print(i, temp)
    else:
        s.add(i)

#8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list. Ask user to enter a number
# in the range of 1,50 and make sure if the entered number is even, append it 
# to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each listMake sure once you enter
# all the 5 elements, calculate the sum of the list and return themaximum of the list.

even_list =  []
odd_list = []
i = 0
print("Enter enter a number in range 1 to 50 ")
x = int(input()) 
while(i<10):
    if x >= 1 and  x <= 50 :
        if(x % 2 == 0 and len(even_list) <= 5):
            even_list.append(x)
            print("Even List",even_list)
        elif(x % 2 ==1 and len(odd_list) <= 5):
            odd_list.append(x)
            print("Odd List",odd_list)
        else:
            pass
    else: 
        print("Enter a number in range 1-50.")
    i += 1
    print("Enter enter a number in range 1 to 50 ")
    x = int(input())


print("Sums:")
import functools
evenSum = functools.reduce(lambda x,y: x+y, even_list)
oddSum = functools.reduce(lambda x,y : x+y, odd_list)
print(evenSum)
print(oddSum)



#9.Write a program to find out the occurrence of a specific characterfrom an alphanumeric string.
# Sample Expected output:a=5 b=5 c=2

input = "12abcbacbaba344ab"
alphaDict = {}
for item in input:
    if item.isalpha():
        if item not in alphaDict:
            alphaDict.setdefault(item,1)
        else: 
            alphaDict[item] += 1
    else: 
        continue
 
for key,value  in alphaDict.items():
    print(key ," = ", value)
\


#10. Generate and print another tuple whose values are even numbers in the given tuple
input = (1,2,3,4,5,6,7,8,9,10)
x = tuple([i  for i in input if i%2 == 0])
