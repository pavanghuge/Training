#Exercise 9: Reverse a given number and return true if it is the same as the original number

originalNum = 213
number = originalNum
reversedNum = 0
while (number > 0):
    remainder = number % 10
    reversedNum = (reversedNum*10) + remainder 
    number = number // 10
if(reversedNum == originalNum):
    print("True")
else:
    print("False")