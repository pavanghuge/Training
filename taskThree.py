
# 1. Create a list of 10 elements of four different data types like int, string, complex and float.

myList = [1, 3, 4, 2.2, 5.5, (6+7j), "boy","girl",10,21.22]

# 2. Create a list of size 5 and execute the slicing structure
myList1 = [1,2,3,4,5]
print(myList1[:4])

# 3. Write a program to get the sum and multiply of all the items in a given list.

myList = [1,2,3,4,5,6,7]
sum = 0
multi = 1 
for i in myList:
    sum += i
    multi *= i

print("Sum = ",sum, " Multiplication = ",multi)  



# 4. Find the largest and smallest number from a given list.

myList = [3,6,5,2,1,9]
print("Max = ", max(myList), " Min = ", min(myList))


# 5.Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

myList = [1,2,3,4,5,6,7,8,9]
newList = []
for i in myList:
    if i % 2 == 1:
        newList.append(i)
print(newList)


#6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and 30 (both included).

x = range(1,31)[:5]
y = range(1,31)[25:31]

sqr = []

for i in x:
    sqr.append(i*i)

for i in y:
    sqr.append(i*i)
     
print(sqr)


# 7. Write a program to replace the last element in a list with another list
#Sample input: [1,3,5,7,9,10], [2,4,6,8]Expected output: [1,3,5,7,9,2,4,6,8]

x = [1,3,5,7,9,10]
y = [2,4,6,8]

x.extend(y)
print(x)




# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input:a={1:10,2:20} b={3:30,4:40} Expected output: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}

a.update(b)
print(a)


#9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1and n(both 1 and n included).
# Sample input:n=5 Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
print("Enter a number: ")
n =int(input())

sqr_dict = {x : x**2 for x in range(1,n+1) }
print(sqr_dict)

#10. Write a program which accepts a sequence of comma-separated numbers from console andgenerates a list and a tuple which 
# contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

print("Enter a comma separated sequence of numbers:") 
x = input()

print(list(x.split(',')),tuple(x.split(',')))













