# Exercise 1: Given two integer numbers return their product. 
# If the product is greater than 1000, then return their sum

num1 = input("number1 ")
print("\n")
num2 = input("number2 ")

if(num1*num2 >1000):
    print("The result is ", num1 + num2)

else:
    print("The result is ", num1 * num2)
